"""Make the SCHISM mesh of the Perth coast used by the notebooks (hgrid.gr3).

The water area is a box off Perth minus the land in ETOPO 2022 (elevation >= 0),
with Rottnest (in two parts: ETOPO separates its western end) and Garden
islands as holes. gmsh fills it with triangles that are about 400 m long at the
coast and grow to about 2.5 km offshore. Depths are interpolated from ETOPO, and
the west, north and south sides of the box are the open boundary.

Usage: python make_mesh.py etopo15s_perth.nc hgrid.gr3

Needs gmsh, shapely, scipy, matplotlib and pylibs-ocean (pip install gmsh shapely
pylibs-ocean). make_mesh.py is not needed to run the notebooks: hgrid.gr3 is
committed next to it.
"""

import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from pylib import schism_grid
from scipy.interpolate import RegularGridInterpolator
from shapely.geometry import Polygon, box
from shapely.ops import unary_union

# Domain (degrees): the west, north and south sides are open boundaries
WEST, EAST, SOUTH, NORTH = 115.0, 115.85, -32.6, -31.6
# Element size: at the coast, offshore, and the distance over which it grows
SIZE_COAST, SIZE_OFFSHORE, GROWTH_DISTANCE = 0.004, 0.025, 0.2
# Coastline simplification tolerance and smallest island kept (degrees, degrees^2)
SIMPLIFY, MIN_ISLAND_AREA = 0.002, 2e-5
# Minimum depth at open boundary nodes (m): SCHISM stops on a dry open boundary
MIN_OPEN_BOUNDARY_DEPTH = 2.0


def water_polygon(lon, lat, elevation) -> Polygon:
    """The sea inside the domain: the box minus land (elevation >= 0)."""
    contours = plt.contourf(lon, lat, elevation, levels=[0, 1e4])
    land = unary_union(
        [
            Polygon(ring).buffer(0)
            for path in contours.get_paths()
            for ring in path.to_polygons()
            if len(ring) > 3
        ]
    )
    plt.close("all")
    water = box(WEST, SOUTH, EAST, NORTH).difference(land)
    water = max(getattr(water, "geoms", [water]), key=lambda p: p.area)
    islands = [i for i in water.interiors if Polygon(i).area > MIN_ISLAND_AREA]
    return Polygon(water.exterior, islands).simplify(SIMPLIFY, preserve_topology=True)


def on_domain_edge(p, q) -> bool:
    """True if the segment p-q lies along a side of the domain box."""
    return (p[0] == q[0] and p[0] in (WEST, EAST)) or (
        p[1] == q[1] and p[1] in (SOUTH, NORTH)
    )


def triangulate(water: Polygon) -> tuple[np.ndarray, np.ndarray]:
    """Nodes (lon, lat) and triangles (0-based, counter-clockwise) from gmsh."""
    import gmsh

    gmsh.initialize()
    gmsh.option.setNumber("General.Verbosity", 1)
    geo = gmsh.model.geo

    def add_loop(coords):
        coords = list(coords)[:-1]
        points = [geo.addPoint(x, y, 0) for x, y in coords]
        lines = [
            geo.addLine(points[i], points[(i + 1) % len(points)])
            for i in range(len(points))
        ]
        return geo.addCurveLoop(lines), lines, coords

    outer, outer_lines, outer_coords = add_loop(water.exterior.coords)
    islands = [add_loop(ring.coords) for ring in water.interiors]
    geo.addPlaneSurface([outer] + [loop for loop, _, _ in islands])
    geo.synchronize()

    # Element size grows with the distance to the coast (not to the open boundary)
    coast = [
        line
        for i, line in enumerate(outer_lines)
        if not on_domain_edge(
            outer_coords[i], outer_coords[(i + 1) % len(outer_coords)]
        )
    ] + [line for _, lines, _ in islands for line in lines]
    field = gmsh.model.mesh.field
    distance = field.add("Distance")
    field.setNumbers(distance, "CurvesList", coast)
    field.setNumber(distance, "Sampling", 20)
    size = field.add("Threshold")
    field.setNumber(size, "InField", distance)
    field.setNumber(size, "SizeMin", SIZE_COAST)
    field.setNumber(size, "SizeMax", SIZE_OFFSHORE)
    field.setNumber(size, "DistMin", 0.01)
    field.setNumber(size, "DistMax", GROWTH_DISTANCE)
    field.setAsBackgroundMesh(size)
    for option in (
        "MeshSizeExtendFromBoundary",
        "MeshSizeFromPoints",
        "MeshSizeFromCurvature",
    ):
        gmsh.option.setNumber(f"Mesh.{option}", 0)
    gmsh.model.mesh.generate(2)

    tags, xyz, _ = gmsh.model.mesh.getNodes()
    _, _, element_nodes = gmsh.model.mesh.getElements(2)
    gmsh.finalize()

    index = {tag: i for i, tag in enumerate(tags)}
    triangles = np.vectorize(index.get)(element_nodes[0].reshape(-1, 3))
    used = np.unique(triangles)
    renumber = np.full(len(tags), -1)
    renumber[used] = np.arange(len(used))
    nodes = xyz.reshape(-1, 3)[used, :2]
    triangles = renumber[triangles]
    # SCHISM wants counter-clockwise elements
    x, y = nodes[triangles, 0], nodes[triangles, 1]
    clockwise = (x[:, 1] - x[:, 0]) * (y[:, 2] - y[:, 0]) < (x[:, 2] - x[:, 0]) * (
        y[:, 1] - y[:, 0]
    )
    triangles[clockwise] = triangles[clockwise][:, [0, 2, 1]]
    return nodes, triangles


def main(etopo_file: str, hgrid_file: str) -> None:
    etopo = xr.open_dataset(etopo_file).sel(
        longitude=slice(WEST - 0.05, EAST + 0.05),
        latitude=slice(SOUTH - 0.05, NORTH + 0.05),
    )
    lon, lat, elevation = etopo.longitude.values, etopo.latitude.values, etopo.z.values

    nodes, triangles = triangulate(water_polygon(lon, lat, elevation))
    interpolate = RegularGridInterpolator((lat, lon), elevation)
    depth = -interpolate(nodes[:, ::-1])  # SCHISM depths are positive down

    grid = schism_grid()
    grid.x, grid.y, grid.dp = nodes[:, 0], nodes[:, 1], depth
    grid.np, grid.ne = len(nodes), len(triangles)
    grid.elnode = np.c_[triangles, np.full(len(triangles), -2)]
    grid.i34 = np.full(len(triangles), 3)
    # One open boundary, from the coast at the north-east corner round the sea to
    # the coast at the south-east corner; the coast and islands are land
    ne_corner = nodes[np.isclose(nodes[:, 1], NORTH)][:, 0].max()
    se_corner = nodes[np.isclose(nodes[:, 1], SOUTH)][:, 0].max()
    grid.compute_bnd(bxy=[ne_corner, se_corner, NORTH, SOUTH])
    open_nodes = np.concatenate(grid.iobn)
    grid.dp[open_nodes] = np.maximum(grid.dp[open_nodes], MIN_OPEN_BOUNDARY_DEPTH)
    grid.write_hgrid(hgrid_file, fmt=1, Info="Perth coast, ETOPO 2022, gmsh")
    print(
        f"{hgrid_file}: {grid.np} nodes, {grid.ne} elements, "
        f"{grid.nob} open boundary ({grid.nobn[0]} nodes), {grid.nlb} land boundaries"
    )


if __name__ == "__main__":
    matplotlib.use("Agg")
    main(*sys.argv[1:3])
