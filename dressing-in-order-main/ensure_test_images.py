# import os
# import shutil
# import zipfile
# import gdown

# def download_and_extract(folder, zip_filename, file_id):
#     os.makedirs(folder, exist_ok=True)
#     zip_path = os.path.join(folder, zip_filename)
#     url = f"https://drive.google.com/uc?id={file_id}"

#     print(f"⬇️ Downloading {zip_filename} from Google Drive...")
#     gdown.download(url, zip_path, quiet=False)

#     print(f"📦 Unzipping {zip_filename}...")
#     with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#         zip_ref.extractall(os.path.join(folder, 'images'))
#     os.remove(zip_path)
#     print("✅ Extraction complete.")

# def read_lst_file(lst_path):
#     with open(lst_path, 'r') as f:
#         return set(line.strip().split()[0] for line in f if line.strip())

# def copy_required_images(lst_set, source_dir, target_dir):
#     os.makedirs(target_dir, exist_ok=True)
#     copied = 0
#     for root, _, files in os.walk(source_dir):
#         for file in files:
#             rel_path = os.path.relpath(os.path.join(root, file), source_dir)
#             if rel_path.replace("\\", "/") in lst_set or file in lst_set:
#                 src = os.path.join(root, file)
#                 dst = os.path.join(target_dir, file)
#                 os.makedirs(os.path.dirname(dst), exist_ok=True)
#                 shutil.copy2(src, dst)
#                 copied += 1
#     print(f"✅ Copied {copied} images to {target_dir}")

# # === CONFIG ===
# deepfashion = os.path.join('datasets', 'deepfashion')
# images_folder = os.path.join(deepfashion, 'images')
# test_lst_file = os.path.join(deepfashion, 'test.lst')
# test_output = os.path.join('data', 'test')

# # STEP 1 (optional): Uncomment to redownload and unzip images if needed
# # download_and_extract(deepfashion, 'images.zip', '1U2PljA7NE57jcSSzPs21ZurdIPXdYZtN')

# # STEP 2: Copy required test images based on test.lst
# test_images = read_lst_file(test_lst_file)
# copy_required_images(test_images, images_folder, test_output)
import os
import shutil

# === Paths ===
base_dir = os.path.abspath(os.path.dirname(__file__))
deepfashion_images = os.path.join(base_dir, 'datasets', 'deepfashion', 'images')
test_lst_path = os.path.join(base_dir, 'datasets', 'deepfashion', 'test.lst')
test_output_dir = os.path.join(base_dir, 'data', 'test')

os.makedirs(test_output_dir, exist_ok=True)

# === Read test.lst filenames ===
with open(test_lst_path, 'r') as f:
    test_files = [line.strip().split()[0] for line in f if line.strip()]

missing = 0
copied = 0

for rel_path in test_files:
    rel_path = rel_path.replace("/", os.sep)
    source = os.path.join(deepfashion_images, rel_path)
    target = os.path.join(test_output_dir, os.path.basename(rel_path))
    
    if os.path.exists(source):
        shutil.copy2(source, target)
        copied += 1
    else:
        print(f"❌ Missing: {source}")
        missing += 1

print(f"\n✅ Copied: {copied} images")
if missing:
    print(f"⚠️ Still missing: {missing} images")
else:
    print("🎉 All test images found and copied successfully.")
