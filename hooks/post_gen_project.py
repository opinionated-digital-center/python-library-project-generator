#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file_or_dir(filepath):
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.isfile(full_path):
        os.remove(full_path)
    else:
        shutil.rmtree(full_path)


paths_to_remove = []
if "{{ cookiecutter.create_author_file|lower }}" != "y":
    paths_to_remove += [
        "AUTHORS.rst",
        os.path.join("docs", "authors.rst"),
    ]

if "{{ cookiecutter.command_line_interface|lower }}" == "none":
    paths_to_remove += [
        os.path.join("{{ cookiecutter.project_package_name }}", "cli.py"),
        "behave4cmd0",
        os.path.join("features", "steps", "use_steplib_behave4cmd.py"),
        os.path.join("features", "cli.feature"),
    ]

if "{{ cookiecutter.open_source_license }}" == "Not open source":
    paths_to_remove += [
        "LICENSE",
    ]

if "{{ cookiecutter.hosting|lower }}" == "gitlab":
    paths_to_remove += [
        ".github",
    ]
else:
    paths_to_remove += [
        ".gitlab-ci.yml",
        ".releaserc",
    ]

for path in paths_to_remove:
    remove_file_or_dir(path)
