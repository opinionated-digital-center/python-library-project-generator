#!/usr/bin/env python
"""Tests for `{{ cookiecutter.project_package_name }}` package."""
{%- if cookiecutter.use_pytest != "y" %}

import unittest
{%- endif %}

from {{ cookiecutter.project_package_name }} import core


{% if cookiecutter.use_pytest == "y" -%}
def test_hello_world():
    """Test hello world."""
    assert core.hello_world() == "Hello world!"
{% else -%}
class Test{{ cookiecutter.project_package_name|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_package_name }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_hello_world(self):
        """Test hello world."""
        assert core.hello_world() == "Hello world!"
{% endif -%}
