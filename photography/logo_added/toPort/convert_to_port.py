import os
import shutil
from PIL import Image

# Current folder ('.') and output folder 'landToport'
folder_path = '.'
output_folder = 'landToport'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to rotate image by 90 degrees
def rotate_image(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            img = img.rotate(90, expand=True)  # Rotate 90 degrees
            img.save(output_path, format='JPEG')  # Save the image as JPG
            print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Iterate over all the files in the current folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.jpg'):  # Ensure we only process .jpg (case-insensitive)
        image_path = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, filename)
        rotate_image(image_path, output_path)

print("Rotation completed!")

# Path one level up from the current folder ('.')
parent_folder_one_up = os.path.abspath(os.path.join(folder_path, '..'))

# Move all files from landToport to one level up
for filename in os.listdir(output_folder):
    src_path = os.path.join(output_folder, filename)
    dst_path = os.path.join(parent_folder_one_up, filename)
    try:
        shutil.move(src_path, dst_path)
        print(f"Moved {filename} to {parent_folder_one_up}")
    except Exception as e:
        print(f"Error moving {filename}: {e}")

print("All files moved to the parent folder one level up!")
