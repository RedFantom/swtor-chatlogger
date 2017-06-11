# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE

# Originally written for the GSF Parser, modified for this program
import collections
import tkinter.messagebox as mb
import os
import configparser
import ast
from tools.utilities import get_temp_directory


class ColorScheme(object):
    def __init__(self):
        self.default_colors = collections.OrderedDict()
        self.default_colors["whisper"] = ["#a582ff", "#ffffff"]
        self.default_colors["group"] = ["#cc87f3", "#ffffff"]
        self.default_colors["emote"] = ["#ff8022", "#ffffff"]
        self.default_colors["self"] = ["#ff0000", "#ffffff"]
        self.default_colors["yell"] = ["#ff7397", "#ffffff"]
        self.default_colors["say"] = ["#00a4ff", "#ffffff"]
        self.default_colors["general"] = ["#00a4ff", "#ffffff"]
        self.default_colors["pvp"] = ["#00a4ff", "#ffffff"]
        self.default_colors["ops"] = ["#ff6000", "#ffffff"]
        self.default_colors["system"] = ["#e6ff00", "#ffffff"]
        self.current_scheme = self.default_colors

    def __setitem__(self, key, value):
        self.current_scheme[key] = value

    def __getitem__(self, key):
        return list(self.current_scheme[key])

    def set_scheme(self, name, custom_file=(os.path.join(get_temp_directory(), "event_colors.ini"))):
        if name == "default":
            self.current_scheme = self.default_colors
        elif name == "custom":
            cp = configparser.ConfigParser()
            print(custom_file)
            cp.read(custom_file)
            print(cp.sections())
            try:
                current_scheme = cp["colors"]
                for key, value in list(current_scheme.items()):
                    self.current_scheme[key] = ast.literal_eval(value)
            except configparser.NoSectionError as e:
                self.current_scheme = self.default_colors
                mb.showinfo("Info", "Failed to load custom colors, default colors have been loaded as "
                                    "custom color scheme.")
                mb.showerror("Info", "The specific error:\n{0}".format(e))
        else:
            raise ValueError("Expected default or custom, got %s" % name)

    def write_custom(self):
        custom_file = os.path.join(get_temp_directory(), "event_colors.ini")
        cp = configparser.RawConfigParser()
        try:
            cp.add_section("colors")
        except configparser.DuplicateSectionError:
            pass
        for key, value in list(self.current_scheme.items()):
            cp.set('colors', key, value)
        with open(custom_file, "w") as file_obj:
            cp.write(file_obj)
