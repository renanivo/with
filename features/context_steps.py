# -*- coding: utf-8 -*-
import os
import subprocess

from lettuce import step, world


@step(u'I am out of any context')
def out_of_any_context(step):
    world.process = None


@step(u'I type `with (.+)`$')
def type_with(step, command):
    world.process = subprocess.Popen(
        "{cwd}/with.py {command}".format(cwd=os.getcwd(), command=command),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )


@step(u'I type `(.+?)`$')
def type(step, command):
    world.stdout, world.stderr = world.process.communicate(command)


@step(u'I see an output equal to the command `(.+)`')
def then_i_see_the_output_of_the_command_git_status(step, command):
    cmd_out = subprocess.check_output(command, shell=True)
    assert cmd_out in world.stdout, world.diff(cmd_out, world.stdout)
