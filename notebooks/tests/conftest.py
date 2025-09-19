import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

import requests

DATA_REPO = "rom-py/rompy-test-data"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
GITHUB_API_RELEASES = f"https://api.github.com/repos/{DATA_REPO}/releases/latest"

# Add the tests directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def download_and_extract_data():
    print("Downloading test data from rompy-test-data repo...")
    # Get latest release info
    resp = requests.get(GITHUB_API_RELEASES)
    resp.raise_for_status()
    release = resp.json()
    # Find the zipball URL
    zip_url = release["zipball_url"]
    # Download the zip
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "data.zip")
        with requests.get(zip_url, stream=True) as r:
            r.raise_for_status()
            with open(zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        # Extract only the data/ directory
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            # Find the top-level directory in the zip
            top_level = zip_ref.namelist()[0].split("/")[0]
            # Extract data/ to DATA_DIR
            for member in zip_ref.namelist():
                if member.startswith(f"{top_level}/data/"):
                    zip_ref.extract(member, tmpdir)
            src_data_dir = os.path.join(tmpdir, top_level, "data")
            if os.path.exists(DATA_DIR):
                shutil.rmtree(DATA_DIR)
            shutil.copytree(src_data_dir, DATA_DIR)
    print("Test data downloaded and extracted.")


# Only download if data dir is missing or empty
if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
    try:
        download_and_extract_data()
    except Exception as e:
        print(f"Failed to download test data: {e}", file=sys.stderr)
        sys.exit(1)
