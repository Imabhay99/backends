# download_fasion_pairs_test.py
import gdown
import os

# Ensure the "data" folder exists
os.makedirs("data", exist_ok=True)

# Google Drive link and destination path
url = "https://drive.google.com/uc?id=12fZKGf0kIu5OX3mjC-C3tptxrD8sxm7x"
output = "data/fasion-pairs-test.csv"

# Download the file
gdown.download(url, output, quiet=False)
# python download_fasion_pairs_test.py
