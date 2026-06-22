import os

# 📂 Folder containing your .txt files
label_folder = "Masked_face/labels_coco"

# Loop through all files
for file in os.listdir(label_folder):
    if file.endswith(".txt"):
        file_path = os.path.join(label_folder, file)
        
        # Open and clear content
        open(file_path, 'w').close()

print("✅ All .txt files are now empty.")