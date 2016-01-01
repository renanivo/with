import sys
import asyncio
import subprocess
from prompt_toolkit.shortcuts import prompt_async


@asyncio.coroutine
def main():
    while True:
        cmd = sys.argv[1]
        sub = yield from prompt_async('{}… '.format(cmd), patch_stdout=True)
        call = '{cmd} {sub}'.format(cmd=cmd, sub=sub)
        subprocess.check_call(call, shell=True)
