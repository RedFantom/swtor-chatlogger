# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os
from tools import ColorsWindow


class SettingsWindow(tk.Toplevel):
    def __init__(self, master, settings):
        tk.Toplevel.__init__(self, master)
        self.resizable(False, False)
        self.wm_title("SWTOR Chat Logger: Settings")
        self.grab_set()
        self.settings = settings
        self.save_to_files = tk.BooleanVar()
        self.save_to_files_box = ttk.Checkbutton(self, text="Save chat log to files", variable=self.save_to_files,
                                                 command=self.save_settings)
        self.path_entry_label = ttk.Label(self, text="Default log save path: ")
        self.path_entry = ttk.Entry(self, width=60, font=("default", 10))
        self.path_browse = ttk.Button(self, text="Browse", command=self.browse_path, style="TButton")
        self.colors_label = ttk.Label(self, text="Chat categories color scheme:")
        self.color_scheme = tk.StringVar()
        self.colors_default_box = ttk.Radiobutton(self, text="Default", value="default", variable=self.color_scheme,
                                                  command=self.save_settings)
        self.colors_custom_box = ttk.Radiobutton(self, text="Custom", value="custom", variable=self.color_scheme,
                                                 command=self.save_settings)
        self.colors_custom_button = ttk.Button(self, text="Customize",
                                               command=lambda: ColorsWindow(master, master.colors))

        self.update_widgets()
        self.grid_widgets()

    def grid_widgets(self):
        self.save_to_files_box.grid(column=0, row=0, columnspan=2, sticky="nw", padx=5, pady=5)
        self.path_entry_label.grid(column=0, row=1, sticky="w", padx=5, pady=(0, 5))
        self.path_entry.grid(column=0, row=2, sticky="nswe", padx=5, pady=(0, 5), columnspan=4)
        self.path_browse.grid(column=4, row=2, sticky="nswe", padx=5, pady=(0, 5))
        self.colors_label.grid(column=0, row=3, sticky="w", padx=5, pady=(0, 5))
        self.colors_default_box.grid(column=1, row=3, sticky="w", padx=(0, 5), pady=(0, 5))
        self.colors_custom_box.grid(column=2, row=3, sticky="w", padx=(0, 5), pady=(0, 5))
        self.colors_custom_button.grid(column=4, row=3, sticky="w", padx=5, pady=(0, 5))

    def save_settings(self):
        dictionary = {"settings": {
            "colors": self.color_scheme.get(),
            "folder": self.path_entry.get(),
            "timeout": 0.5,
            "save": self.save_to_files.get()
        }}
        self.settings.read_dict(dictionary)
        self.settings.write_settings()

    def browse_path(self):
        self.path_entry.config(state=tk.NORMAL)
        path = fd.askdirectory(master=self, title="Choose directory", initialdir=self.settings["folder"])
        if not os.path.exists(path):
            self.path_entry.config(state=tk.DISABLED)
            return
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(tk.END, path)
        self.path_entry.config(state=tk.DISABLED)
        self.save_settings()

    def update_widgets(self):
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(tk.END, self.settings["folder"])
        self.save_to_files.set(self.settings["save"])
        self.color_scheme.set(self.settings["colors"])
