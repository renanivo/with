import os
import subprocess

from behave import given, when, then


@given('I am out of any context')
def out_of_any_context(context):
    if hasattr(context, 'process'):
        context.process.kill()
        context.process = None


@when('I type `with {command}`')
def type_with(context, command):
    context.process = subprocess.Popen(
        "{cwd}/with.py {command}".format(cwd=os.getcwd(), command=command),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )


@when('I type `{subcommand}`')
def type(context, subcommand):
    context.stdout, context.stderr = context.process.communicate(subcommand)


@then('I see an output equal to the command `{command}`')
def then_i_see_the_output_of_the_command_git_status(context, command):
    cmd_out = subprocess.check_output(command, shell=True).decode('utf-8')
    assert cmd_out in context.stdout
