# PDF to Image Converter

This script converts a PDF file into individual PNG images, one for each page, using the `pdf2image` library.

## Prerequisites

- Python 3.x
- Required Python package:
  - `pdf2image`
- System dependency:
  - Poppler (`poppler-utils`) must be installed on your system. 
    - On Windows: Download and install from a package manager or add to PATH.
    - On macOS: `brew install poppler`
    - On Linux: `sudo apt-get install poppler-utils` (Ubuntu/Debian) or equivalent for other distributions.

## Installation

1. Install the required Python package:
   ```bash
   pip install pdf2image
   ```

2. Ensure Poppler is installed and accessible in your system's PATH.

## Usage

1. Place your PDF file (e.g., `Nitisatkam.pdf`) in the same directory as the script.
2. Update the `pdf_path` variable in the script to match your PDF file name.
3. Run the script:
   ```bash
   python pdf_to_image.py
   ```

The script will:
- Create an output folder named `pdf_images` (if it doesn't exist).
- Convert each page of the PDF to a PNG image with 300 DPI.
- Save the images as `page_1.png`, `page_2.png`, etc., in the `pdf_images` folder.
- Print a confirmation message indicating the number of pages saved.

## Code Explanation

- **Input**: A PDF file specified by `pdf_path`.
- **Output**: PNG images saved in the `pdf_images` folder.
- **Library**: Uses `pdf2image.convert_from_path` to convert PDF pages to images.
- **DPI**: Set to 300 for high-quality images (adjustable in the script).
- **File Naming**: Images are named sequentially as `page_1.png`, `page_2.png`, etc.

## Example

For a PDF named `Nitisatkam.pdf` with 5 pages, running the script will create:
```
pdf_images/
  ├── page_1.png
  ├── page_2.png
  ├── page_3.png
  ├── page_4.png
  ├── page_5.png
```

And output:
```
Saved 5 pages as images in 'pdf_images'
```

## Notes

- Ensure the PDF file exists in the specified path.
- Adjust the `dpi` parameter in the script for different image resolutions (higher DPI increases file size).
- The script assumes write permissions in the directory to create the output folder.

## Troubleshooting

- **ModuleNotFoundError**: Ensure `pdf2image` is installed (`pip install pdf2image`).
- **Poppler Error**: Verify Poppler is installed and added to your system's PATH.
- **FileNotFoundError**: Check that the PDF file path is correct.
