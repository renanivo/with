from behave import given, when, then

@given(u'I have "{command}" in my bash history')
def add_to_history(context, command):
    raise NotImplementedError(u'STEP: Given I have "git status" in my bash history')

@when(u'I press <{key}>')
def press(context, key):
    raise NotImplementedError(u'STEP: When I type `st` and press <tab>')

@then(u'I see that "{subcommand}" was filled')
def step_impl(context, subcommand):
    raise NotImplementedError(u'STEP: Then I see that "status" was filled')
