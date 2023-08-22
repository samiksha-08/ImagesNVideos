#copying a .jpg file for every .txt file present in the folder

import os
import shutil

# Specify the folder paths for txt files and jpg files
txt_folder_path = 'C:/Users/NHI658/Downloads/labels'
jpg_folder_path = 'C:/Users/NHI658/Downloads/images'

# Iterate over the txt files in the folder
for txt_filename in os.listdir(txt_folder_path):
    if txt_filename.endswith('.txt'):
        # Construct the corresponding jpg filename
        jpg_filename = os.path.splitext(txt_filename)[0] + '.jpg'

        # Check if the jpg file exists in the jpg folder
        jpg_filepath = os.path.join(jpg_folder_path, jpg_filename)
        if os.path.isfile(jpg_filepath):
            # Create a copy of the jpg file in the txt folder
            new_jpg_filepath = os.path.join(txt_folder_path, os.path.splitext(txt_filename)[0] + '.jpg')
            shutil.copy2(jpg_filepath, new_jpg_filepath)
            print(f"Copied {jpg_filename} as {os.path.basename(new_jpg_filepath)}")
        else:
            print(f"No corresponding jpg file found for {txt_filename}")
