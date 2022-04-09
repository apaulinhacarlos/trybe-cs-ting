import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, "r") as file:
            file_content = file.read()
            return file_content.split("\n")

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


# print(txt_importer("statics/arquivo_teste.txt"))
