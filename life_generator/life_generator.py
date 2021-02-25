# Name:  Joshua Fogus
# Last Modified:  February 9, 2021
# Description:  An application which generates and filters lists of toys.

import sys
import tkinter as tk
from gui.application import Application
from cli.application import application


def life_generator(data_file, filter_file):
    if not filter_file:
        # Start the GUI implementation
        root = tk.Tk()
        app = Application(data_file, root)
        app.mainloop()
    else:
        # Star the CLI implementation
        application(data_file, filter_file)


if __name__ == "__main__":
    file_path = None

    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    life_generator("amazon_co-ecommerce_sample.csv", file_path)
