Feature: Say Hello world
    As a cli user
    I want to print "Hello world!"
    In order to say to the world how happy I am

    Scenario:
        Given a new working directory
        When I run "{{cookiecutter.project_slug}} hello"
        Then it should pass with
            """
            Hello world!
            """
