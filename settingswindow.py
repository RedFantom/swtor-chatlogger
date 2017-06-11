import tkinter as tk
from tkinter import ttk


class SettingsWindow(tk.Toplevel):
    def __init__(self, master, settings_obj=None):
        tk.Toplevel.__init__(self, master)
