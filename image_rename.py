# sajal Debnath
# 5th april 2025

import os

folder_path = "./Dataset/Original/CSF/CSF_Training/4-AD"

new_folder_path = "./Dataset/Renamed/CSF_Training"

# Get a sorted list of all image files in the folder
files = sorted(os.listdir(folder_path))

# Loop through files and rename them
# change start value for starting from 1, 91, 162, and ... 
for index, filename in enumerate(files, start=216):
    # Extract file extension (e.g., .png, .jpg)
    ext = os.path.splitext(filename)[1]
    
    # Define the new filename
    new_name = f"CSF-{index}{ext}"
    
    # Full file paths
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(new_folder_path, new_name)

    # Rename the file
    os.rename(old_path, new_path)

print("Renaming complete!")
