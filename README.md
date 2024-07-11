# SANITIZE APP  

This Python script removes EXIF and other metadata from an image and save the result to a new jpg file, retaining the ICC color profile if present. The output file will have the same name as the input file with '_sanitized' appended.  

This method also removes Content Credentials.   

## Installation   
Requires Python and Pillow.   
Clone this repo and run ```pip install -r requirements.txt``` will install Pillow.   

## sanitize.py  
Main python script.  

:param input_image_path: Path to the input image file  
:param output_image_path: Path to save the sanitized image file  

./your_script.py /path/to/your/directory  

./your_script.py  


## sanitize.bat  
Batch file is for calling sanitize.py. Add path to Python and batch file in the windows environment paths and call sanitize from anywhere.  


## LICENSE  
GNU General Public License v3.0  