# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  An implementation of a CLI for the life generator
#               application.

from modules.toy_list import ToyList
from modules.data_reader import data_reader
from modules.filter_reader import filter_reader
from modules.csv_writer import csv_writer


def application(data_file, filter_file):
    """ Accepts a path to a file which contains data and a path
        to a file which contains filters. Outputs the filtered
        data to a csv. """

    # Load data
    model = ToyList(data_reader(data_file))

    # Load filters
    filters = filter_reader(filter_file)

    category = filters[1]
    num_results = filters[2]

    # Filter the data
    model.filter_by_category(category)
    model.filter_by_rank(num_results)

    # Prepare data for writing to CSV
    headers = [
        "input_item_type",
        "input_item_category",
        "input_number_to_generate",
        "output_item_name",
        "output_item_rating",
        "output_item_num_reviews"
    ]
    output_fields = [
        "product_name",
        "average_review_rating",
        "number_of_reviews"
    ]

    output_data = model.get_display_formatted(output_fields)
    csv_data = [["toys", category, num_results] + toy for toy in output_data]

    # Write to CSV
    csv_writer(headers, csv_data, "output.csv")


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
