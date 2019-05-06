"""Alphabetizer for a roster"""
class Person:
    """Class for a Person"""
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def __str__(self):
        return '{0} {1} <{2}>'.format(self.first, self.last, self.email)

    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.first, self.last, self.email)

    def __eq__(self, other):
        return self.first == other.first and self.last == other.last and self.email == other.email

def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.first < b.first:
        return True
    if a.first == b.first:
        if a.last < b.last:
            return True
    return False

def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """

    if a.last < b.last:
        return True
    if a.last == b.last:
        if a.first < b.first:
            return True
    return False

def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """

    # https://stackoverflow.com/questions/46126797/compare-the-elements-of-a-list-in-python

    for i in range(1, len(roster)):
        if roster[i-1] == roster[i]:
            return True
        if not ordering(roster[i-1], roster[i]):
            return False
    return True


def alphabetize(roster, ordering):
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """

    # https://d2l.msu.edu/d2l/le/content/661872/viewContent/7156494/View
    # https://www.geeksforgeeks.org/merge-sort/
    # https://stackoverflow.com/questions/752308/split-list-into-smaller-lists


    # Merge Sort

    cost = 0

    if len(roster) > 1:

        # Split the roster into two lists
        a = roster[len(roster) // 2:]
        b = roster[:len(roster) // 2]

        # Alphabetize both lists and increment cost
        cost += alphabetize(a, ordering)[1]
        cost += alphabetize(b, ordering)[1]

        i = j = k = 0

        # Copying the alphabetical string over
        while i < len(a) and j < len(b):
            if ordering(a[i], b[j]):
                roster[k] = a[i]
                i += 1
            else:
                roster[k] = b[j]
                j += 1
            k += 1
            cost += 1

        # Append any leftover string to roster
        while k < len(roster):
            if i < len(a):
                roster[k] = a[i]
                i += 1
            if j < len(b):
                roster[k] = b[j]
                j += 1
            k += 1

    return (list(roster), cost)

