import os
import sys

from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import prompt_async

from withtool.config import get_config


def get_prompt(command):
    config = get_config()

    try:
        sub = yield from prompt_async(
            '{}… '.format(command),
            patch_stdout=True,
            history=get_history(config['history_dir'], command),
            auto_suggest=AutoSuggestFromHistory()
        )
    except EOFError:
        print('bye')
        sys.exit()

    return sub


def get_history(history_dir, command):
    filename = os.path.join(history_dir, "{}.history".format(command))

    if not os.path.isfile(filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.close()

    return FileHistory(filename)
