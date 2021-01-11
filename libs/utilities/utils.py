"""
Common helper methods
"""

import os
import re
import sys


def get_os():
    return sys.platform


def get_project_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path_sep = os.path.sep
    regexed_directory = re.search(
        r'(?P<root_dir>(.)*)(?:(' + re.escape(path_sep) + 'tests|' + re.escape(path_sep) + 'libs)(.)*)',
        str(current_directory)
    )
    return regexed_directory.group('root_dir')

