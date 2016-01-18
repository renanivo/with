import sys
import asyncio

from withtool.prompt import get_prompt
from withtool.subprocess import run


@asyncio.coroutine
def main():
    command = sys.argv[1]

    while True:
        sub = yield from get_prompt(command)
        call = '{cmd} {sub}'.format(cmd=command, sub=sub)
        run(call)
