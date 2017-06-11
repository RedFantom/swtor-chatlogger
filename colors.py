# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE

# Originally written for the GSF Parser, modified for this program
import collections
import tkinter.messagebox
import os
import configparser
import ast
import utilities


class ColorScheme(object):
    def __init__(self):
        self.default_colors = collections.OrderedDict()
        self.default_colors["whisper"] = ["purple", "white"]
        self.default_colors["group"] = []
        self.current_scheme = collections.OrderedDict()

    def __setitem__(self, key, value):
        self.current_scheme[key] = value

    def __getitem__(self, key):
        try:
            return list(self.current_scheme[key])
        except KeyError:
            tkinter.messagebox.showerror("Error", "The requested color for %s was not found, "
                                                  "did you alter the event_colors.ini file?" % key)
            return ['#ffffff', '#000000']
        except TypeError:
            tkinter.messagebox.showerror("Error", "The requested color for %s was could not be "
                                                  "type changed into a list. Did you alter the "
                                                  "event_colors.ini file?" % key)
            return ['#ffffff', '#000000']

    def set_scheme(self, name, custom_file=(os.path.join(utilities.get_temp_directory(), "events_colors.ini"))):
        if name == "default":
            self.current_scheme = self.default_colors
        elif name == "custom":
            cp = configparser.RawConfigParser()
            cp.read(custom_file)
            try:
                current_scheme = dict(cp.items("colors"))
                for key, value in list(current_scheme.items()):
                    self.current_scheme[key] = ast.literal_eval(value)
            except configparser.NoSectionError:
                self.current_scheme = self.default_colors
                tkinter.messagebox.showinfo("Info", "Failed to load custom colors, default colors have been loaded as "
                                                    "custom color scheme.")
        else:
            raise ValueError("Expected default, pastel or custom, got %s" % name)

    def write_custom(self):
        custom_file = os.path.join(utilities.get_temp_directory(), "event_colors.ini")
        cp = configparser.RawConfigParser()
        try:
            cp.add_section("colors")
        except configparser.DuplicateSectionError:
            pass
        for key, value in list(self.current_scheme.items()):
            cp.set('colors', key, value)
        with open(custom_file, "w") as file_obj:
            cp.write(file_obj)
