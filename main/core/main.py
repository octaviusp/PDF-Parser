from .splitter import split_pdf_in_images
from .text_extractor_ocr import extract_text
from tabula import read_pdf, convert_into


def main(pdf_path: str) -> bool:
    """Main function of pdf parser.
    The begin of the process.

    Args:
        pdf_path (str): pdf file path

    Returns:
        bool: if the process was success or not.

    """

    images_splitted = split_pdf_in_images(pdf_path)

    if images_splitted:

        return get_text(pdf_path)

    return ""


def get_text(pdf_path: str) -> list:
    """Get all text from a pdf with 
    Tesseract Engine.

    Args:
        pdf_path (str): pdf path file

    Returns:
        list: a list of texts
    """

    text_list = extract_text(pdf_path)
    return text_list


def get_table(pdf_path: str, pages=all) -> str:
    """Get table from a pdf with tabula library.

    Args:
        pdf_path (str): pdf path file

    Returns:
        str: string containing the extracted tables
    """

    data_frame = read_pdf(pdf_path, pages=pages,
                          java_options="-Dfile.encoding=UTF8", multiple_tables=True)

    return data_frame


def convert_into_csv(pdf_path, pages=all, output_name="output.csv") -> bool:
    """Convert a pdf table into csv

    Args:
        pdf_path (str): pdf path file

    Returns:
        bool: if the transformation was successful or not.
    """
    try:

        convert_into(pdf_path, output_name, pages=pages)
        return True

    except:
        return False


###################
# TESTING PURPOSES #
"""
    -------------
    Hardcoded

data_frame1 = str(list(get_table("./original.pdf", pages=3))[0]).split("\\r")
data_frame2 = str(list(get_table("./original.pdf", pages=4))[0]).split("\\r")
data_frame3 = get_table("./original.pdf", pages=5)

text_frame3 = get_text("./original.pdf", pages=5)
print(text_frame3)
with open("results1.txt", "w") as file:
    for data in data_frame1:
        file.write(str(data) + '\n')
    file.close()
    
with open("results2.txt", "w") as file:
    for data in data_frame2:
        file.write(str(data) + "\n")
    file.close()

with open("results3.txt", "w") as file:
    for data in data_frame3:
        file.write(str(data) + "\n")
    file.close()
#print(convert_into_csv("./0.pdf", output_name="0.csv"))
#print(convert_into_csv("./0.pdf", output_name="0.csv"))
#print(convert_into_csv("./1.pdf", output_name="1.csv"))
#####################"""
