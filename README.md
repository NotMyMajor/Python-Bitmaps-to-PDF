# Python-Bitmaps-to-PDF
This script serves as both a function and a standalone program to convert a folder of .bmp files to a single PDF.

# Documentation

Welcome to bmp2pdf! A quick little script to convert a folder of .bmp files into a single PDF.
This script can be used as a function or run by itself. 
If you choose to run the file by itself, check the options at the bottom. 

# THIS PROGRAM REQUIRES NATSORT, FPDF, AND CV2. IF YOU WISH TO USE THIS PROGRAM STANDALONE, YOU WILL ALSO NEED TKINTER.

natsort is used to sort the list of .bmp files in a more natural way. This means that .bmp files will be sorted alphabetically or numerically in the fashion "1, 2, 3, 4, 5..." rather than the default "1, 10, 11...2, 20, 21...etc.".
fpdf is used to create and write the final PDF.
cv2 is used to process and handle the image files.
tkinter is used in the standalone process for easy folder selection.

The function requires the following arguments:
bmp_folder: This should be a directory path (string) leading to the directory containing the .bmp files you want to convert.
save_path: This should be a directory path (string) leading to the directory in which you want to save the PDF. This can be the same as bmp_path or different.
pdf_name: This should be a string containing the desired name of your PDF. If this name is missing the .pdf extension, it will automatically be added.
save_png: Boolean. This script converts the .bmp images to .png images before adding them to the PDF. If you wish to save the .png versions of the images in addition to the PDF, set this value to 1.

