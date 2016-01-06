import os

from prompt_toolkit.history import FileHistory


def get_history(history_dir, command):
    filename = os.path.join(history_dir, "{}.history".format(command))

    if not os.path.isfile(filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.close()

    return FileHistory(filename)
