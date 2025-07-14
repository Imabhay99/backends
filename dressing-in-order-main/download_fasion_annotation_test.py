import os
import gdown

os.makedirs("data", exist_ok=True)

url = "https://drive.google.com/uc?id=1MxkVFFtNsWFshQp_TA7qwIGEUEUIpYdS"
output = "data/fasion-annotation-test.csv"

gdown.download(url, output, quiet=False)
