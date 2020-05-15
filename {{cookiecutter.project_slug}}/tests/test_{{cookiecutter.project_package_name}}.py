#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_package_name }}` package."""
from {{ cookiecutter.project_package_name }} import core


def test_hello_world():
    """Test hello world."""
    assert core.hello_world() == "Hello world!"
