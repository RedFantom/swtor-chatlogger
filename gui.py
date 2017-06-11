# -*- coding: utf-8 -*-

# Copyright (C) 2017 by RedFantom
# For license see LICENSE
import tkinter as tk
from tkinter import ttk
from ttkthemes.themed_tk import ThemedTk
from colors import ColorScheme
import ocr
from settingswindow import SettingsWindow


class MainWindow(ThemedTk):
    """
    Main program GUI window
    """

    def __init__(self):
        """
        Create all widgets and call grid_widgets() to set them up
        """
        ThemedTk.__init__(self)
        self.set_theme("arc")
        self.colors = ColorScheme()
        self.protocol("WM_DELETE_WINDOW", self.exit)
        self.bind("<Configure>", self.grid_widgets)
        self.resizable(width=False, height=False)
        self.wm_title("SWTOR Chat Logger")
        # Create menu and add it to window
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        # Add file menu and its subcommands
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Open file", command=self.open_file)
        self.filemenu.add_command(label="Save to file", command=self.save_to_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        # Add edit menu and its subcommands
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu.add_command(label="Preferences", command=self.show_settings)
        self.menu.add_cascade(label="Edit", menu=self.editmenu)
        # Add all main widgets
        self.text_widget = tk.Listbox(self, font=("Consolas", 10), height=16, width=60)
        self.text_widget.bind("<<ListBoxSelect>>", self.set_highlight_color)
        # Create variables for keeping track of lines
        self.line = 0
        self.line_types = {}
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=self.scrollbar.set)
        self.start_logging_button = ttk.Button(self, text="Start logging", command=self.start_stop_logging)
        self.grid_widgets()

    def grid_widgets(self, *args):
        self.text_widget.grid(row=0, column=0, columnspan=2, sticky="nswe")
        self.start_logging_button.grid(row=1, column=0, sticky="nswe")
        self.scrollbar.grid(row=0, column=2, sticky="ns")

    def exit(self):
        self.destroy()
        exit()

    def start_stop_logging(self):
        pass

    def start_logging(self):
        pass

    def stop_logging(self):
        pass

    def save_to_file(self):
        pass

    def read_from_file(self):
        pass

    def open_file(self):

        self.read_from_file()

    def show_settings(self):
        SettingsWindow(self)

    def insert_into_listbox(self, type, string, line=None):
        if not line:
            line = self.line
        self.text_widget.insert(line, string)
        self.text_widget.itemconfig(line, foreground=self.colors[type][0], background=self.colors[type][1])
        self.line_types[line] = type
        self.line += 1

    def set_highlight_color(self, *args):
        print(self.text_widget.curselection())

if __name__ == '__main__':
    window = MainWindow()
    window.insert_into_listbox("whisper", "some great string")
    window.mainloop()
