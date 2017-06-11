# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE

# Originally written for the GSF Parser, modified for this program
import os
import sys

debug = False


def get_temp_directory():
    """
    Returns the absolute path to the directory that is to be used by the GSF Parser for the temporary files.
    :return: str
    """
    if debug:
        return os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    if sys.platform == "win32":
        import tempfile
        path = os.path.abspath(os.path.join(tempfile.gettempdir(), "..", "SWTOR Chat Logger"))
        try:
            os.makedirs(path)
        except OSError:
            pass
        return path
    elif sys.platform == "linux":
        path = "/var/tmp/swtorchatlogger"
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    else:
        raise ValueError("Unsupported platform: %s" % sys.platform)


def get_assets_directory():
    return os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "assets"))
