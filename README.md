# SANITIZE APP  

Remove EXIF data from an image and save the result to a new file,
retaining the ICC color profile if present. The output file will
have the same name as the input file with '_sanitized' appended.  


## sanitize.py  
Main python script.  

:param input_image_path: Path to the input image file  
:param output_image_path: Path to save the sanitized image file  

./your_script.py /path/to/your/directory  

./your_script.py  


## sanitize.bat  
Batch file is for calling sanitize.py. Add path to python file in windows environment paths and call sanitize from anywhere.  