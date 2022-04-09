from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file_content = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": (file_content),
    }

    instance.enqueue(file_data)
    print(file_data)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        file_removed = instance.dequeue()
        print(
            f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso"
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
