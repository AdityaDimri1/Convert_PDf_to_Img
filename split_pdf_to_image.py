from pdf2image import convert_from_path
import os

# Path to your PDF file
pdf_path = "Nitisatkam.pdf"

# Folder to save images
output_folder = "pdf_images/"
os.makedirs(output_folder, exist_ok=True)

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300)  

# Save each page as an image
for i, image in enumerate(images):
    image_path = os.path.join(output_folder, f"page_{i+1}.png")
    image.save(image_path, "PNG")

print(f"Saved {len(images)} pages as images in '{output_folder}'")
