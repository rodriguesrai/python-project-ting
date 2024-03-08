from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_lines = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    if file_info not in instance._queue:
        instance.enqueue(file_info)
        print(file_info, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        item = instance.dequeue()
        print(
            f"Arquivo {item['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout,
        )


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        item = instance.search(position)
        print(item, file=sys.stdout)
