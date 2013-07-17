Feature: Perform transfer
    As a user, I want to transfer money from my account (source) to my friend's account (sink) so that my friend got the money.

    Scenario: Transfer 100 baths
        Given I have money 1000 baths
        And my friend have 0 baths
        When I transfer money 100 baths
        Then I should have 900 baths
        Then my friend should have 100 baths

