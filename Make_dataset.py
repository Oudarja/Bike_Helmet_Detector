import os
import random
import shutil

# 📂 Source folder (your images)
src_folder = "Human Faces Dataset/Real Images"

# 📂 Destination folders
dst_img_folder = "output/images"
dst_lbl_folder = "output/labels"

# create folders if not exist
os.makedirs(dst_img_folder, exist_ok=True)
os.makedirs(dst_lbl_folder, exist_ok=True)

# get all image files
images = [f for f in os.listdir(src_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# randomly select 500 images
selected_images = random.sample(images, 500)

for img_name in selected_images:
    src_path = os.path.join(src_folder, img_name)
    
    # copy image
    shutil.copy(src_path, os.path.join(dst_img_folder, img_name))
    
    # create empty txt file
    txt_name = os.path.splitext(img_name)[0] + ".txt"
    txt_path = os.path.join(dst_lbl_folder, txt_name)
    
    open(txt_path, 'w').close()  # creates empty file

print("✅ Done! 500 images + empty labels created.")