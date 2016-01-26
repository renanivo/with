import asyncio
import sys

from docopt import docopt

import withtool
from withtool.prompt import get_prompt
from withtool.subprocess import run


@asyncio.coroutine
def main():
    """
Usage: with (--version | <command>)

Arguments:
    command     The command to use as prefix to your context.

Options:
    -h --help   Show this screen.
    --version   Show the current version.
    """
    arguments = docopt(main.__doc__)

    if arguments.get('--version'):
        print('with {}'.format(withtool.__version__))
        sys.exit()

    while True:
        sub = yield from get_prompt(arguments['<command>'])
        call = '{cmd} {sub}'.format(cmd=arguments['<command>'], sub=sub)
        run(call)
