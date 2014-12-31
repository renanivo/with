Feature: Autocomplete
    As a developer
    I want a autocomplete
    So that I don't need to time the entire sentence time after time

    Scenario: History autocomplete
        Given I have "git status" in my bash history
        And I type `with git`
        When I type `st` and press <tab>
        Then I see that "status" was filled
