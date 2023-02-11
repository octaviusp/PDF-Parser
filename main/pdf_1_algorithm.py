# Working
from core import main
from helpers import tools

# FALTA REALIZAR 2DA TABLA


def execute(pdf_type_1_path: str) -> bool:
    """ETL for pdf type 1 specified in docs.

    Args:
        pdf_type_1_path (str): pdf path file

    Returns:
        bool: whether the algorithm worked or not.
    """

    # Getting first table with tabula
    first_table = main.get_table(pdf_path=pdf_type_1_path, pages=3)[0]
    # Getting second table with tabula
    second_table = main.get_table(pdf_path=pdf_type_1_path, pages=[4, 6])[0]

    # an array with the data organized and structured, normalized.
    data_normalized = []

    # for every data that we receive from the generator
    for data in format_table(first_table):
        # format the data of course, also
        # we gonna search the necessary fields
        formatted_and_found = format_and_search_field(data.upper())
        # if formatted_and_found (it means that the field was found in relevant data)
        data_normalized.append(
            formatted_and_found) if formatted_and_found else None

    # after gathering all data and formatting it, print organized tuples,
    # [:-1] is 'cause a extra field was returned and we don't need it.
    print_organized_tuples(data_normalized[:-1])
    return True


def format_table(table):
    """Format a table into string, splitting and returning cleaned parts.

    Args:
        table (Data frame): Data frame object from tabula

    Yields:
        str: strings and if the string matches with a specific rules, string formatted.
    """

    # Convert into string then splitting between \r char
    table = str(table).split("\\r")

    # for every string in the table converted into string
    for data in table:
        # make a generator of data retrieved, also before it
        # we gonna clean nif and postal code fields,
        # remember, this is the algorithm for pdf_1 so, it is the unique that will contain this.
        yield clean_nif_and_postal_code(data)


def format_and_search_field(data: str) -> tuple:
    """Format data but also looking if the data is in data to extract dictionary.
    If isn't in data to extract dictionary, ignore this data, otherwise, gather it.

    Args:
        data (str): Data into string

    Returns:
        tuple: a tuple that is data formatted with key and value.
    """

    for data_to_extract in tools.data_to_extract_from_first_table:

        if (data.find(data_to_extract) != -1):

            data_value = data.replace(data_to_extract, "")
            data_keyword = data.replace(data_value, "")
            return (data_value, data_keyword)

    return ()


def clean_nif_and_postal_code(data: str) -> str:
    """Search if the string matches with hardcode string,
        if matches, remove it.

    Args:
        data (str): data string

    Returns:
        str: string cleaned.
    """

    if (data.find("N.I.F/C.I.F .:") != -1):
        data = data.replace("N.I.F/C.I.F .:", "")
    elif (data.find("COD. POSTAL:") != -1):
        data = data.replace("COD. POSTAL:", "")

    return data


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
