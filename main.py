import splitter
import text_extractor_ocr
import tabula


def main(pdf_path: str) -> bool:
    """Main function of pdf parser.
    The begin of the process.

    Args:
        pdf_path (str): pdf file path

    Returns:
        bool: if the process was success or not.

    """

    images_splitted = splitter.split_pdf_in_images(pdf_path)

    if images_splitted:

        get_text(pdf_path)

        return True

    return False


def get_text(pdf_path: str) -> list:
    """Get all text from a pdf with 
    Tesseract Engine.

    Args:
        pdf_path (str): pdf path file

    Returns:
        list: a list of texts
    """

    text_list = text_extractor_ocr.extract_text(pdf_path)
    return text_list


def get_table(pdf_path: str) -> str:
    """Get table from a pdf with tabula library.

    Args:
        pdf_path (str): pdf path file

    Returns:
        str: string containing the extracted tables
    """

    tables = tabula.read_pdf(pdf_path)
    return tables
