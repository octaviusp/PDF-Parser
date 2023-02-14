import tabula


def main():
    path = "2.pdf"

    tables = tabula.io.read_pdf(path, pages=8)

    print(tables)


if __name__ == "__main__":
    main()
