def exists_word(word, instance):
    result = []
    occurrences = []

    for i in range(len(instance)):
        file_data = instance.search(i)
        for line_index, line in enumerate(file_data["linhas_do_arquivo"]):
            if word.casefold() in line.casefold():
                occurrences.append({"linha": line_index + 1})
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })
        occurrences = []

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
