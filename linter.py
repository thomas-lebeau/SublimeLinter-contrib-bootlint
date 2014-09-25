#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Thomas Lebeau
# Copyright (c) 2014 Thomas Lebeau
#
# License: MIT
#

"""This module exports the Bootlint plugin class."""

from SublimeLinter.lint import Linter, util


class Bootlint(Linter):

    """Provides an interface to bootlint."""

    syntax = 'html'
    cmd = 'bootlint'
    regex = (
        r'^.+?:\s'  # filename
        r'(?P<message>.+)'
    )
    tempfile_suffix = 'html'
    error_stream = util.STREAM_BOTH

    def split_match(self, match):
        """
        Extract and return values from match.

        We override this method because bootlint errors does not have
        a line number so error can be placed at the beginning of the code.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None and message:
            line = 0
            col = 0

        return match, line, col, error, warning, message, near
