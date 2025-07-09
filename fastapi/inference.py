import sys
import os
import requests
import cloudinary
import cloudinary.uploader
sys.path.append(os.path.abspath("../dressing-in-order-main"))

from dressing_in_order_generate import generate_tryon


# Setup Cloudinary
cloudinary.config(
    cloud_name="drxs4yu5j",
    api_key="792394351774396",
    api_secret="FlYEHsvl6g_sKNSm8P46hf1GdYg",
)

# CLOUDINARY_CLOUD_NAME = drxs4yu5j
# CLOUDINARY_API_KEY = 792394351774396
# CLOUDINARY_API_SECRET= FlYEHsvl6g_sKNSm8P46hf1GdYg

# Use your DIOR model here
from dressing_in_order_generate import generate_tryon  # Stub (to be implemented)

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(response.content)

def run_tryon_from_urls(person_url, cloth_url):
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    person_path = "uploads/person.png"
    cloth_path = "uploads/cloth.png"
    output_path = "output/result.png"

    download_image(person_url, person_path)
    download_image(cloth_url, cloth_path)

    generate_tryon(person_path, cloth_path, output_path)

    result = cloudinary.uploader.upload(output_path)
    return result["secure_url"]
