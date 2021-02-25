# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A drop-down menu.

import tkinter as tk


def dropdown_menu(parent, label, variable, options):
    """ Creates a dropdown menu attached to the given
        parent, with the given label, storing the result in the given
        variable, and offering the given options.  Returns a tuple
        of the label and menu"""
    tk_label = tk.Label(parent, text="{}: ".format(label))
    tk_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 4))

    tk_menu = tk.OptionMenu(parent, variable, "", *options)
    tk_menu.grid(row=1, column=1, sticky=tk.W, pady=(0, 4))

    return tk_label, tk_menu


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")