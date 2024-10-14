import os
from PIL import Image
import cairosvg

# Convert the SVG signature to PNG format using CairoSVG
signature_png = "signature_converted.png"
if not os.path.exists(signature_png):  # Check if the PNG already exists
    cairosvg.svg2png(url="signature.svg", write_to=signature_png)

# Load the signature (already converted to PNG)
signature = Image.open(signature_png)
signature = signature.resize((180, 150))  # Adjust size if necessary

# Create a new folder called "edited" to store the processed images
edited_folder = "edited"
if not os.path.exists(edited_folder):
    os.makedirs(edited_folder)

# Loop through all .jpg files in the current folder
for filename in os.listdir("."):
    if filename.lower().endswith(".jpg") and not filename.startswith("._"):  # Check for .jpg files and ignore hidden files
        try:
            # Open the current photo
            photo = Image.open(filename)
            position = (photo.width - 180, photo.height - 150)
            # Determine the orientation of the image
            # if photo.width > photo.height:
            #     # Landscape: place logo in the bottom right corner
            #     position = (photo.width - 180, photo.height - 150)
            # else:
            #     # Portrait: place logo in the bottom left corner
            #     position = (10, photo.height - 150)  # Adjust "10" for padding from the left edge if needed

            # Paste the signature onto the photo at the determined position
            photo.paste(signature, position, signature)

            # Save the final image to the "edited" folder with the same filename
            edited_path = os.path.join(edited_folder, filename)
            photo.save(edited_path)

            print(f"Processed {filename} successfully.")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All valid .jpg images have been processed and saved in the 'edited' folder.")
