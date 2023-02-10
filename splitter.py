from pdf2image import convert_from_path


def split_pdf_in_images(_pdf_path: str) -> list:
    """Split a pdf in each image per page.

    Args:
        _pdf_path (str): the path of the pdf file.

    Returns:
        list: a list of the image partitions path.
    """

    images_path = []

    try:
        # Open with pdf2image
        doc = convert_from_path(_dpi=500, pdf_path=_pdf_path)

        # Splitting pdf in images per page.
        for n, page in enumerate(doc):
            route = f"./pdf_parts/{n}.pdf"
            page.save(route, "PDF")
            images_path.append(route)

        return images_path

    except:

        return []
