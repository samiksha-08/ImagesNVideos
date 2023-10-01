import os
from PIL import Image

# Folder containing the images
input_folder = "images"

# New extension for the images (e.g., ".jpg" or ".png")
new_extension = ".jpg"

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can add more extensions if needed)
    if filename.endswith(".jfif"):
        # Open the image
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Generate a new filename with the desired extension
            new_filename = os.path.splitext(filename)[0] + new_extension
            # Save the image with the new filename and extension
            img.save(os.path.join(input_folder, new_filename))
            print(f"Converted {filename} to {new_filename}")
