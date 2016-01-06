import sys
import asyncio
import subprocess

from prompt_toolkit.shortcuts import prompt_async
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from withtool.config import get_config
from withtool.prompt import get_history


@asyncio.coroutine
def main():
    command = sys.argv[1]
    config = get_config()

    while True:
        sub = yield from prompt_async(
            '{}… '.format(command),
            patch_stdout=True,
            history=get_history(config['history_dir'], command),
            auto_suggest=AutoSuggestFromHistory()
        )
        call = '{cmd} {sub}'.format(cmd=command, sub=sub)
        subprocess.check_call(call, shell=True)
