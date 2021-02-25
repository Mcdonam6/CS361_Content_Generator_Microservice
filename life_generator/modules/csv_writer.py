# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  A function which writes headers and data to a csv.

import csv


def csv_writer(headers, data, file_path):
    """ Accepts an array of data, which should have length 3 and an optional
        file path to which the data should be written. """

    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(headers)
        # All data must be strings to be written
        for toy in data:
            writer.writerow([str(attr) for attr in toy])


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
