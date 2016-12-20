import os
import sys

from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import prompt_async
from prompt_toolkit.key_binding import manager
from prompt_toolkit import AbortAction
from slugify import slugify

from withtool.config import get_config


kbmanager = manager.KeyBindingManager.for_prompt()
registry = kbmanager.registry
manager.load_basic_system_bindings(registry)


def get_prompt(command):
    config = get_config()
    sub = ''

    try:
        sub = yield from prompt_async(
            '{}… '.format(command),
            patch_stdout=True,
            history=get_history(config['history_dir'], command),
            key_bindings_registry=registry,
            on_abort=AbortAction.RETRY,
            auto_suggest=AutoSuggestFromHistory()
        )
    except EOFError:
        print('bye')
        sys.exit()

    return sub


def get_history(history_dir, command):
    safe_name = slugify(command)
    filename = os.path.join(history_dir, "{}.history".format(safe_name))

    if not os.path.isfile(filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.close()

    return FileHistory(filename)
