from ting_file_management.file_management import txt_importer
import os
import sys


def process(path_file, instance):
    file_name = os.path.basename(path_file)

    if file_name in instance:
        print(f"Arquivo {file_name} já importado", file=sys.stderr)
        return


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
