# Working
from core import main
from helpers import tools


def execute(pdf_type_1_path: str) -> bool:
    """ETL for pdf type 1 specified in docs.

    Args:
        pdf_type_1_path (str): pdf path file

    Returns:
        bool: whether the algorithm worked or not.
    """
    first_table = main.get_table(pdf_path=pdf_type_1_path, pages=3)[0]
    second_table = main.get_table(pdf_path=pdf_type_1_path, pages=[4, 6])[0]

    data_normalized = []

    for data in format_table(first_table):
        formatted = format_field(data)
        data_normalized.append(formatted) if formatted else None

    print_organized_tuples(data_normalized[:-1])


def format_table(table):
    # Convert intro string then splitting between \r char
    table = str(table).split("\\r")

    for data in table:
        yield clean_nif_and_postal_code(data)


def format_field(data: str) -> tuple:

    for data_to_extract in tools.data_to_extract_from_first_table:

        if (data.find(data_to_extract) != -1):

            data_value = data.replace(data_to_extract, "")
            data_keyword = data.replace(data_value, "")
            return (data_value, data_keyword)

    return ()


"""     data_keyword = data.replace(keyword, "")
    data_value = data.replace(data_keyword, "")

    return (data_keyword, data_value) """


def clean_nif_and_postal_code(data: str) -> str:

    if (data.find("N.I.F/C.I.F .:") != -1):
        data = data.replace("N.I.F/C.I.F .:", "")
    elif (data.find("COD. POSTAL:") != -1):
        data = data.replace("COD. POSTAL:", "")

    return data


def print_organized_tuples(data_normalized: tuple):
    for data in data_normalized:
        print(f"- {data[1]} {data[0]}")


execute("C:/Users/Pavón/PDF-Parser/main/original.pdf")
