def exists_word(word, instance):
    result = []

    for item in instance._queue:
        file_name = item["nome_do_arquivo"]
        lines_with_word = []

        for i, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": i})

        if lines_with_word:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": lines_with_word,
                }
            )

    return result


def search_by_word(word, instance):
    result = []

    for item in instance._queue:
        file_name = item["nome_do_arquivo"]
        occurrences = []

        for i, line_content in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line_content.lower():
                occurrences.append({"linha": i, "conteudo": line_content})

        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )

    return result
