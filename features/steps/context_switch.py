import os
import pexpect

from behave import given, when, then


@given('I am out of any context')
def out_of_any_context(context):
    if hasattr(context, 'process'):
        context.process.kill(9)
        context.process = None


@when('I type `with {command}`')
def type_with(context, command):
    context.process = pexpect.spawn(
        "{cwd}/bin/with {command}".format(cwd=os.getcwd(), command=command)
    )


@when('I type `{subcommand}`')
def type(context, subcommand):
    context.process.sendline(subcommand)


@then('I see "{expected}" in the output')
def then_i_see_the_output_of_the_command_git_status(context, expected):
    context.process.expect(expected)
    assert expected in context.process.after.decode('utf-8')
