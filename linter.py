#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Authors:
# Thomas Lebeau
# Patrick Ziegler
#
# Copyright (c) 2015
#
# License: MIT
#

"""This module exports the Bootlint plugin class."""

from SublimeLinter.lint import PythonLinter, util


class Bootlint(PythonLinter):

    """Provides an interface to bootlint."""

    syntax = 'html'
    cmd = 'bootlint'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.12.0'
    regex = (
        r'^.+?:'  # filename
        r'(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>[E])|(?P<warning>[W]))\d+ '
        r'(?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = 'html'
    error_stream = util.STREAM_BOTH
    check_version = True
