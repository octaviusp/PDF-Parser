# Working
from core import main
from helpers import tools


def execute(pdf_type_2_path: str) -> bool:
    """ETL for pdf type 2 specified in docs.

    Args:
        pdf_type_2_path (str): pdf path file

    Returns:
        bool: whether the algorithm worked or not.
    """
    tables = []
    # Getting tables with tabula
    tables.append(main.get_table(pdf_path=pdf_type_2_path, pages=5))
    tables.append(main.get_table(pdf_path=pdf_type_2_path, pages=7))
    tables.append(main.get_table(pdf_path=pdf_type_2_path, pages=8))

    for n, table in enumerate(tables):
        table = str(table)
        with open(f"results_2_pdf_{n}.txt", "w") as file:
            file.write(table)
            file.close()

    print("\n\n----------")
