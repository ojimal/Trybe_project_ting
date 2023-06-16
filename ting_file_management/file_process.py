import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(0, len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None
    file_lines = txt_importer(path_file)
    out = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_lines),
        'linhas_do_arquivo': file_lines,
    }
    instance.enqueue(out)
    print(out, file=sys.stdout)


def remove(instance):
    if not instance:
        print('Não há elementos', file=sys.stdout)
        return None
    file_removed = instance.dequeue()['nome_do_arquivo']
    print(f'Arquivo {file_removed} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    if not 0 <= position < len(instance):
        print('Posição Inválida', file=sys.stderr)
        return
    queue = instance.search(position)
    print(queue, file=sys.stdout)
