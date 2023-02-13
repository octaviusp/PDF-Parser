# Working
from core import main
from helpers import tools

# FALTA REALIZAR 2DA TABLA


def execute(pdf_type_2_path: str) -> bool:
    """ETL for pdf type 2 specified in docs.

    Args:
        pdf_type_2_path (str): pdf path file

    Returns:
        bool: whether the algorithm worked or not.
    """
    tables = []
    # Getting first table with tabula
    tables.append(main.get_table(pdf_path=pdf_type_2_path, pages=5)[0])
    # Getting second table with tabula
    tables.append(main.get_table(pdf_path=pdf_type_2_path, pages=7)[0])
    # Getting third table table with tabula
    tables.append(main.get_table(pdf_path=pdf_type_2_path, pages=8)[0])
    
    for n, table in enumerate(tables):
        table = str(table)
        with open(f"results_2_pdf_+{n}.txt", "w") as file:
            file.write(table)
            file.close()
    

def print_organized_tuples(data_normalized: tuple) -> None:
    """Print tuples in an organized form.

    Args:
        data_normalized (tuple): data in tuple form, but isn't organized.

    Returns:
        tuple: a generator with tuples organized.
    """

    for data in data_normalized:
        print(f"- {data[1]} {data[0]}")
        # if we wanna retrieval this data to use,we could write
        # yield (data[1], data[0])
# pages: 5,7,8

execute("2.pdf")