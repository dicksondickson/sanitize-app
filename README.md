# SANITIZE APP  

This Python script removes EXIF and other metadata from an image and save the result to a new jpg file, retaining the ICC color profile if present. The output file will have the same name as the input file with '_sanitized' appended.  

This method also removes Content Credentials.   


## Installation   
Requires Python and Pillow.   
Clone this repo and run ```pip install -r requirements.txt``` will install Pillow.   


## sanitize.py  
Main python script.  

Copy the Python script to the folder with images you want to sanitize and run ```python sanitize.py```. A ```sanitized``` sub folder will be created and the output files will have the same name as the input file with '_sanitized' appended.   

You can also run ```python sanitize.py /path/to/your/images/directory```.   
 

## sanitize.bat  
Batch file is for calling sanitize.py in Windows from any folder. Add the path to the Python script and batch file in the windows environment paths and call sanitize from anywhere.  


## LICENSE  
GNU General Public License v3.0  