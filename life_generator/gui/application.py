# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A GUI for the life generator application.

import tkinter as tk
from tkinter import font

from gui.title import title
from gui.dropdown_menu import dropdown_menu
from gui.text_input import text_input
from gui.button import button

from modules.toy_list import ToyList

from modules.data_reader import data_reader
from modules.csv_writer import csv_writer


class Application(tk.Frame):
    def __init__(self, file, master):
        super().__init__(master)
        self.master = master

        self.model = ToyList(data_reader(file))
        self.category = tk.StringVar(self)
        self.num_results = tk.StringVar(self)
        self.results = []

        self.create_widgets()

    def create_widgets(self):
        """ Creates and styles the widgets for the application. """
        self.grid(padx=16, pady=16)

        title(self, "Life Generator")
        dropdown_menu(self, "Category", self.category, self.model.categories)
        text_input(self, "Number of Results", self.num_results)
        button(self, "Submit", self.generate_results)

    def clear_results(self):
        """ Clears the table of output toys. """
        for cell in self.results:
            cell.grid_remove()

    def generate_results(self):
        """ Creates a table of the top X number of toys from category Y, where
            X and Y are both user selected. """

        # Ensure the table space is clean before displaying
        self.clear_results()

        # Get user input
        category = self.category.get()
        num_results = int(self.num_results.get())

        # Prepare table for display
        table_row = 5
        display_headers = ["product_name", "average_review_rating", "number_of_reviews"]

        for i, field in enumerate(display_headers):
            cell = tk.Message(self, text=field.title().replace("_", " "), font=font.Font(weight="bold"))
            cell.grid(row=table_row, column=i, sticky=tk.W)

        table_row += 1

        # Filter results for display
        self.model.reset_working_data()
        self.model.filter_by_category(category)
        self.model.filter_by_rank(num_results)

        results = self.model.get_display_formatted(display_headers)

        # Display results in table
        for i, toy in enumerate(results):
            for j, attr in enumerate(toy):
                cell = tk.Message(self, text=attr, width=400)
                cell.grid(row=table_row + i, column=j, sticky=tk.W)

                self.results.append(cell)

        # Save output to csv
        save_headers = [
            "input_item_type",
            "input_item_category",
            "input_number_to_generate",
            "output_item_name",
            "output_item_rating",
            "output_item_num_reviews"
        ]
        csv_data = [["toys", category, num_results] + toy for toy in results]
        csv_writer(save_headers, csv_data, "output.csv")


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
