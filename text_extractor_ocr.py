from pytesseract import pytesseract
from os import environ

from dotenv import load_dotenv
load_dotenv(dotenv_path="./private.env")

# Setting tesseract path
pytesseract.tesseract_cmd = environ.get("TESSERACT_ENGINE")


def extract_text(images_path: list) -> list:
    """Text extractor from a list of images.

    Args:
        images_path (list): list of image paths.

    Returns:
        list: a list of text extracted from each image.
    """
    texts = []

    try:
        for image in images_path:
            texts.append(pytesseract.image_to_string(image))

        return texts
    except:
        return [""]
