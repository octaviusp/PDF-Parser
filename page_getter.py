""" from pdf2image import convert_from_path

# NOT WORKING, BUILDING...

doc = convert_from_path(pdf_path="original.pdf",
                        first_page=3, last_page=4, dpi=500, poppler_path="C:/poppler/bin")

for n, page in enumerate(doc):
    page.save(f"{n}.pdf") """
