# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A button to perform an action when clicked.

import tkinter as tk


def button(parent, text, callback):
    """ Creates a button attached to the given parent, with
        the given text and calls the given callback when
        pressed. Returns the button. """
    tk_button = tk.Button(parent, text=text, command=callback)
    tk_button.grid(row=3, column=0, columnspan=5, pady=8)

    return tk_button


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")