import os
import sys

pypi_url = pypi_name = None

try:
    pypi_url = os.environ["PYPI_REPOSITORY_URL"]
except KeyError:
    pass
try:
    pypi_name = os.environ["PYPI_REPOSITORY_NAME"]
except KeyError:
    pass

if not pypi_name or pypi_name == "pypi":
    if pypi_url:
        print(
            f"ERROR: (PYPI_REPOSITORY_NAME = '{pypi_name}', "
            f"PYPI_REPOSITORY_URL = '{pypi_url}') "
            f"When the environment variable PYPI_REPOSITORY_NAME is 'pypi', "
            f"empty or not defined, you must NOT define environment variable "
            f"PYPI_REPOSITORY_URL."
        )
        sys.exit(1)
else:
    if not pypi_url:
        print(
            f"ERROR: (PYPI_REPOSITORY_NAME = '{pypi_name}', "
            f"PYPI_REPOSITORY_URL = '{pypi_url}') "
            f"When the environment variable PYPI_REPOSITORY_NAME is NOT 'pypi', "
            f"empty or not defined, you must also define environment variable "
            f"PYPI_REPOSITORY_URL."
        )
        sys.exit(1)

print("Pypi repository environment variables correctly configured for CI/CD.")
