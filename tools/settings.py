# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE

# Originally written for the GSF Parser, modified for this program
import os
import configparser

from tools import utilities


class Settings(object):
    defaults = {"settings": {
        "colors": "default",
        "folder": os.path.join(os.path.expanduser("~"), "Documents", "Star Wars - The Old Republic", "Chat Logs"),
        "timeout": 0.5,
        "save": True
    }}

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.path = os.path.join(utilities.get_temp_directory(), "settings.ini")
        if not os.path.exists(self.path):
            try:
                os.makedirs(utilities.get_temp_directory())
            except OSError:
                pass
            self.write_defaults()
        self.read_file()

    def __getitem__(self, key):
        try:
            return self.config["settings"][key]
        except KeyError:
            self.write_defaults()
            self.read_file()
            return self.config["settings"][key]

    def __setitem__(self, key, value):
        if key not in self.config["settings"]:
            raise ValueError("Attempted to add a new setting {0} with value {1}".format(key, value))
        self.config["settings"][key] = value
        self.write_settings()

    def write_defaults(self):
        config = configparser.ConfigParser()
        config.read_dict(self.defaults)
        with open(self.path, "w") as fo:
            config.write(fo)

    def write_settings(self):
        with open(self.path, "w") as fo:
            self.config.write(fo)

    def read_dict(self, dictionary):
        self.config.read_dict(dictionary)
        self.write_settings()

    def read_file(self):
        self.config.read(self.path)

