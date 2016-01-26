Feature: Context switching
    As a developer
    I want to switch shell context
    So that I can type less when I use several subcommands

    Background: I am always starting fresh
        Given I am out of any context

    Scenario: Run a command in a context
        When I type `with echo`
        And I type `works`
        Then I see "works" in the output

    Scenario: Create a context command with spaces and slashes
        When I type `with "ls ../"`
        And I type `./`
        Then I see "./:" in the output
