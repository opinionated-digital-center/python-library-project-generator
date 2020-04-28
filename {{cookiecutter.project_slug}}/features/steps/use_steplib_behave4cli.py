# -*- coding: utf-8 -*-
"""
Use behave4cli step library.
"""

from __future__ import absolute_import

# -- REGISTER-STEPS FROM STEP-LIBRARY:
import behave4cli.__all_steps__
import behave4cli.failing_steps
import behave4cli.note_steps
import behave4cli.passing_steps  # noqa: F401
