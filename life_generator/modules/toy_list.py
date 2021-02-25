# Name:  Joshua Fogus
# Last Modified:  February 11, 2021
# Description:  An object for holding and manipulating toy data.
# Note:  Technique for sorting by multiple columns comes from the Python3 documentation
#        at https://docs.python.org/3/howto/sorting.html
# Note2: Technique for flattening a 2-D array via set comprehension inspired by Geeks for Geeks
#        at https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/

from operator import itemgetter


class ToyList:
    def __init__(self, toy_data):
        self.__toy_data = toy_data
        self.__working_data = toy_data
        self.__categories = sorted({
            category
            for toy in self.working_data
            for category in toy['amazon_category_and_sub_category']
            if category
        })

    @property
    def toy_data(self):
        return self.__toy_data

    @property
    def working_data(self):
        return self.__working_data

    @property
    def categories(self):
        return self.__categories

    def get_display_formatted(self, fields):
        """ Accepts an ordered list of fields and returns a list of
            list of those fields for each toy. """
        return [[toy[field] for field in fields] for toy in self.__working_data]

    def reset_working_data(self):
        """ Sets the working data back to the original copy of the data. """
        self.__working_data = self.__toy_data

    def filter_by_category(self, category):
        """ Accepts a category as a string. Filters the working data to contain
            only toys that are in that category. """
        self.__working_data = [toy for toy in self.__working_data if category in toy['amazon_category_and_sub_category']]

    def filter_by_rank(self,rank):
        """ Accepts an integer indicating the top "rank" number of toys after
            which to discard results in the working data. """

        # Implements a "top" algorithm given in the assignment
        self.__multiple_sort((("number_of_reviews", True), ("uniq_id", False)))
        self.__working_data = self.__working_data[:rank * 10]
        self.__multiple_sort((("average_review_rating", True), ("uniq_id", False)))
        self.__working_data = self.__working_data[:rank]

    def __multiple_sort(self, sorting):
        """ Accepts an array of tuples with the first value as a string
            indicating the column on which to sort and the second value
            as a boolean indicating if the sorting should be descending.
            Returns True if the sort was successful, otherwise False.
            Data may be partially sorted of an error is raised. """

        try:
            # Columns in reverse to exploit sort stability which maintains
            # secondary, etc. sorting
            for col, rev in reversed(sorting):
                self.__working_data.sort(key=itemgetter(col), reverse=rev)
            return True
        except KeyError:
            return False


if __name__ == "__main__":
    print("This is not meant to be run as a script. Please import this module.")
