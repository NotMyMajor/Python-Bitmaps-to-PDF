### NotMyMajor/Python-Bitmaps-to-PDF is licensed under the
### GNU General Public License v3.0
### Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
### See COPYING.txt for full licensing information.

### Welcome to bmp2pdf! A quick little script to convert a folder of .bmp files into a single PDF.
### This script can be used as a function or run by itself. 
### If you choose to run the file by itself, check the options at the bottom. 

### THIS PROGRAM REQUIRES NATSORT, FPDF, AND CV2. IF YOU WISH TO USE THIS PROGRAM STANDALONE, YOU WILL ALSO NEED TKINTER.

### natsort is used to sort the list of .bmp files in a more natural way. This means that .bmp files will be sorted alphabetically or numerically in the fashion "1, 2, 3, 4, 5..." rather than the default "1, 10, 11...2, 20, 21...etc.".
### fpdf is used to create and write the final PDF.
### cv2 is used to process and handle the image files.
### tkinter is used in the standalone process for easy folder selection.

### The function requires the following arguments:
### bmp_folder: This should be a directory path (string) leading to the directory containing the .bmp files you want to convert.
### save_path: This should be a directory path (string) leading to the directory in which you want to save the PDF. This can be the same as bmp_path or different.
### pdf_name: This should be a string containing the desired name of your PDF. If this name is missing the .pdf extension, it will automatically be added.
### save_png: Boolean. This script converts the .bmp images to .png images before adding them to the PDF. If you wish to save the .png versions of the images in addition to the PDF, set this value to 1.


# For standalone use.
from tkinter import filedialog

# bmp2pdf function
def bmp2pdf(bmp_folder, save_path, pdf_name, save_png):

    # Import libraries and modules.
    from natsort import os_sorted
    import cv2
    from fpdf import FPDF
    import os

    # Get contents of directory.
    direct_contents = os.listdir(bmp_folder)
    direct_contents_filt = []

    p_sep = os.path.sep

    # Find only files in directory.
    for i in direct_contents:

        if "." in i:

            direct_contents_filt.append(i)

    # Creates list for bitmaps and folder name for png files.
    list_bitmaps = []
    bmp_exist = False
    current_direct = bmp_folder + p_sep
    new_direct = "{}PNG_Files".format(current_direct)
    print(new_direct)

    # Checks to make sure that the png folder doesn't already exist.
    if os.path.isdir(new_direct):

        raise NameError(
            "PNG Folder already exists.\nThis script was likely already run on this folder.")

    # Create the png folder.
    else:
        os.mkdir(new_direct)

    # Iterate through folders in directory, finds the bitmap files in each folder, and converts them to png.
    for n in direct_contents_filt:

        # Does the conversion from .bmp to .png.
        if n.endswith(".bmp"):

            bmp_exist = True
            img = "{}{}{}".format(bmp_folder, p_sep, n)
            image = cv2.imread(img)

            image_name = "{}{}{}".format(new_direct, p_sep, n)
            print("Converting {}".format(image_name))
            image_name = image_name.replace('.bmp', '.png')

            if not os.path.isfile(image_name):
                cv2.imwrite(image_name, image)

            else:
                raise NameError("Converted image already exists.\nPlease delete the existing images and try again.")

            list_bitmaps.append(image_name)

    # This if statement checks to make sure at least one bitmap image was found and converted in the last step.
    if bmp_exist:

        # Sorts bitmaps to make sure they go into the pdf in the right order.
        list_bitmaps_s = os_sorted(list_bitmaps)
        pdf_w = FPDF()

        # Add the .png images to the PDF.
        for thing in list_bitmaps_s:

            print("Adding image {}".format(thing))
            pdf_w.add_page()
            pdf_w.image(thing, 0, 0, 210, 297)

        # Save pdf to folder.
        else:

            if not(pdf_name.endswith(".pdf")):

                file_name_path = save_path + p_sep + pdf_name + ".pdf"
            else:
                file_name_path = save_path + p_sep + pdf_name

            if not os.path.isfile(file_name_path):

                pdf_w.output(file_name_path, "F")
                print("Finished writing pdf")

            else:
                raise NameError("{}\nAlready exists.".format(file_name_path))
        
        # Delete the temporary png files and folder.
        if not(save_png):
            print("Deleting temporary png files...")
            for n in os.listdir(new_direct):
                file_remove = new_direct + p_sep + n
                os.remove(file_remove)
            os.rmdir(new_direct)

        else:
            print("PNG files saved.")

    # Else statement for bitmap file check.
    else:

        print("No .bmp files found.")

def main():
    
    # Standalone use. Set the variables as needed for your use case. bmp_folder and save_path are determined from tkinter filedialogs. save_png can be a boolean value. pdf_name should be a string.
    print("Choose the .bmp file directory.")
    bmp_folder = str(filedialog.askdirectory(title="Select .bmp folder"))
    if not bmp_folder:
        raise ValueError("ERROR: No directory selectd.")
    save_png = 0
    print("Choose PDF save directory.")
    save_path = str(filedialog.askdirectory(title="Select PDF save folder"))
    if not save_path:
        raise ValueError("ERROR: No directory selectd.")
    pdf_name = "your_pdf_name_here.pdf"
    bmp2pdf(bmp_folder, save_path, pdf_name, save_png)
    
if __name__ == "__main__":
    main()
