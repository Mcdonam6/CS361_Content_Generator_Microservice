# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A function which reads csv filters from a file.

import csv


def filter_reader(file_path=None):
    """ Accepts an optional path to a csv file and returns an array
        of filters. """
    if file_path is None:
        file_path = "../input.csv"

    with open(file_path, 'r') as csv_file:
        file_reader = csv.reader(csv_file)

        # Discard headers before reading the data
        next(file_reader)
        data = next(file_reader)

        # Format the data
        data[2] = int(data[2])

    return data


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
