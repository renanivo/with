import sys
import asyncio

from docopt import docopt

from withtool.prompt import get_prompt
from withtool.subprocess import run


@asyncio.coroutine
def main():
    """
Usage: with COMMAND

Arguments:
    COMMAND     the command to use as prefix

Options:
    -h --help
    """
    arguments = docopt(main.__doc__)

    while True:
        sub = yield from get_prompt(arguments['COMMAND'])
        call = '{cmd} {sub}'.format(cmd=arguments['COMMAND'], sub=sub)
        run(call)
