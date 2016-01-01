Feature: Context switching
    As a developer
    I want to switch shell context
    So that I can type less when I use several subcommands

    Scenario: Run a command in a context
        Given I am out of any context
        When I type `with git`
        And I type `status`
        Then I see an output equal to the command `git status`
