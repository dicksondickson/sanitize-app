#!/usr/bin/env python

import argparse
import os
from PIL import Image

def remove_exif(input_image_path, output_image_path):
    """
    Remove EXIF data from an image and save the result to a new file,
    retaining the ICC color profile if present. The output file will
    have the same name as the input file with '_sanitized' appended.

    :param input_image_path: Path to the input image file
    :param output_image_path: Path to save the sanitized image file
    
    ./your_script.py /path/to/your/directory

    ./your_script.py
    
    
    """
    # Open the image file
    imageLoad = Image.open(input_image_path)
    image = imageLoad.convert('RGB')

    # Get the ICC profile if it exists
    icc_profile = image.info.get('icc_profile')

    # Strip EXIF data by getting the image data and creating a new image
    data = list(image.getdata())
    
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    

    # Save the new image without EXIF data and with the ICC profile if present
    if icc_profile:
        image_without_exif.save(output_image_path, icc_profile=icc_profile, progressive=True, quality=95, optimize=True)
    else:
        image_without_exif.save(output_image_path, progressive=True, quality=95, optimize=True)

    # Close the image file handlers
    image.close()
    image_without_exif.close()

    print(f"Image saved to {output_image_path}")

def process_directory(directory_path):
    """
    Process all JPEG images in the given directory to remove EXIF data.

    :param directory_path: Path to the directory containing images
    """
    sanitized_dir = os.path.join(directory_path, 'sanitized')
    os.makedirs(sanitized_dir, exist_ok=True)
    
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(directory_path, filename)
            base, ext = os.path.splitext(filename)
            ext = '.jpg'
            output_image_path = os.path.join(sanitized_dir, f"{base}_sanitized{ext}")
            remove_exif(input_image_path, output_image_path)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Remove EXIF data from all JPEG images in a directory, retaining ICC color profile.')
    parser.add_argument('input_directory', nargs='?', default=os.getcwd(), help='Path to the directory containing images (default: current working directory)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the process_directory function with the provided argument
    process_directory(args.input_directory)
