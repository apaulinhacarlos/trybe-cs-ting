def exists_word(word, instance):
    results = list()

    for index in range(len(instance)):
        word_searched = instance.search(index)
        occurrences = list()

        for line, contents in enumerate(word_searched["linhas_do_arquivo"]):
            if word.lower() in contents.lower():
                occurrences.append({"linha": (line + 1)})

        if len(occurrences):
            results.append(
                {
                    "palavra": word,
                    "arquivo": word_searched["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
