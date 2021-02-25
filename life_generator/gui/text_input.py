# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A text box for accepting free-form user input.

import tkinter as tk


def text_input(parent, label, variable):
    """ creates a text input attached to the given parent, with
        the given label, and storing the result in the given
        variable.  Returns a tuple of the label and input. """
    tk_label = tk.Label(parent, text="{}: ".format(label))
    tk_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 4))

    tk_input = tk.Entry(parent, textvariable=variable)
    tk_input.grid(row=2, column=1, sticky=tk.W, pady=(0, 4))

    return tk_label, tk_input


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")