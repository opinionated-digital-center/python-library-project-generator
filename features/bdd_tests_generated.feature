Feature: Simple BDD tests are generated

    Scenario: directories and files are correctly generated
        Given a new working directory
#        When I run "cookiecutter --overwrite-if-exists --no-input $PWD/.."
        When I run "pwd"
        Then it should pass with
            """
            blah
            """


