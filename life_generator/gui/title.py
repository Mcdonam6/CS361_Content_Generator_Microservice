# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A title label for the application.

import tkinter as tk
from tkinter import font


def title(parent, text):
    """ Creates a title line attached to the given parent,
        with the given text. Returns the label. """
    tk_label = tk.Label(parent, text=text, font=font.Font(size=32, weight="bold"))
    tk_label.grid(row=0, column=0, columnspan=5, pady=(0, 16))

    return tk_label


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")