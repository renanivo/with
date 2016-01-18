import sys
import asyncio
import subprocess

from withtool.prompt import get_prompt


@asyncio.coroutine
def main():
    command = sys.argv[1]

    while True:
        sub = yield from get_prompt(command)
        call = '{cmd} {sub}'.format(cmd=command, sub=sub)
        subprocess.check_call(call, shell=True)
