# import gdown
# import os
# import zipfile

# def download_from_gdrive(folder, filename, file_id, iszip=True):
#     os.makedirs(folder, exist_ok=True)
#     output_path = os.path.join(folder, filename)
#     url = f"https://drive.google.com/uc?id={file_id}"

#     print(f"⬇️ Downloading {filename} from Google Drive...")
#     gdown.download(url, output_path, quiet=False)

#     if iszip and filename.endswith(".zip"):
#         print(f"📦 Unzipping {filename}...")
#         with zipfile.ZipFile(output_path, 'r') as zip_ref:
#             zip_ref.extractall(folder)
#         os.remove(output_path)
#         print(f"✅ Extracted and deleted zip: {filename}")

# # Download files
# download_from_gdrive("data", "testM_lip.zip", "1toeQwAe57LNPTy9EWGG0u1XfTI7qv6b1")
# download_from_gdrive("data", "images.zip", "1U2PljA7NE57jcSSzPs21ZurdIPXdYZtN")
# download_from_gdrive("data", "fasion-pairs-test.csv", "12fZKGf0kIu5OX3mjC-C3tptxrD8sxm7x", iszip=False)
# download_from_gdrive("data", "fasion-annotation-test.csv", "1MxkVFFtNsWFshQp_TA7qwIGEUEUIpYdS", iszip=False)
# download_from_gdrive("data", "standard_test_anns.txt", "19nJSHrQuoJZ-6cSl3WEYlhQv6ZsAYG-X", iszip=False)
import os
import shutil
import zipfile
import gdown

def download_and_extract(folder, zip_filename, file_id):
    os.makedirs(folder, exist_ok=True)
    zip_path = os.path.join(folder, zip_filename)
    url = f"https://drive.google.com/uc?id={file_id}"

    print(f"⬇️ Downloading {zip_filename} from Google Drive...")
    gdown.download(url, zip_path, quiet=False)

    print(f"📦 Unzipping {zip_filename}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(folder, 'images'))
    os.remove(zip_path)
    print("✅ Done extracting.")

def read_lst_file(lst_path):
    with open(lst_path, 'r') as f:
        return set(line.strip().split()[0] for line in f if line.strip())

def copy_required_images(lst_set, source_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    copied = 0
    missing = []

    for root, _, files in os.walk(source_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), source_dir)
            if rel_path.replace("\\", "/") in lst_set:
                src = os.path.join(root, file)
                dst = os.path.join(target_dir, rel_path)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                copied += 1
            elif file in lst_set:
                src = os.path.join(root, file)
                dst = os.path.join(target_dir, file)
                shutil.copy2(src, dst)
                copied += 1

    print(f"✅ Copied {copied} images to {target_dir}")
    return copied

# === CONFIG ===
base = os.path.dirname(os.path.abspath(__file__))
deepfashion = os.path.join(base, 'datasets', 'deepfashion')
images_folder = os.path.join(deepfashion, 'images')

train_lst_file = os.path.join(deepfashion, 'train.lst')
test_lst_file = os.path.join(deepfashion, 'test.lst')

train_output = os.path.join(deepfashion, 'train')
test_output = os.path.join(deepfashion, 'test')

# === IMAGE ZIP ID (DeepFashion In-shop Images) ===
image_zip_id = "1U2PljA7NE57jcSSzPs21ZurdIPXdYZtN"  # Change to correct one if needed
zip_filename = "images.zip"

# === RUN ===
download_and_extract(deepfashion, zip_filename, image_zip_id)

train_images = read_lst_file(train_lst_file)
test_images = read_lst_file(test_lst_file)

copy_required_images(train_images, images_folder, train_output)
copy_required_images(test_images, images_folder, test_output)

print("🎉 All done!")
