""" Create a Deque data structure with standard functions """

######################
# Deque.py
######################

# http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaDequeinPython.html#lst-dequecode


class Deque:
    """
    A double-ended queue
    """

    def __init__(self):
        """
        Initializes an empty Deque
        """

        self.items = []

    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The size of the Deque
        """

        return len(self.items)

    def peek_front(self):
        """
        Looks at, but does not remove, the first element
        :return: The first element
        """

        # If Deque is empty, raise an error
        if self.is_empty():
            raise IndexError()

        return self.items[0]

    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        """

        # If Deque is empty, raise an error
        if self.is_empty():
            raise IndexError()

        return self.items[-1]

    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """

        self.items.insert(0, e)

    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """

        self.items.append(e)

    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        """

        # If Deque is empty, raise an error
        if self.is_empty():
            raise IndexError()

        return self.items.pop(0)

    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        """

        # If Deque is empty, raise an error
        if self.is_empty():
            raise IndexError()

        return self.items.pop()

    def clear(self):
        """
        Removes all elements from the Deque
        """

        self.items = []

    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        """

        # Yield returns the value of e
        for e in self.items:
            yield e

    def extend(self, other):
        """
        Takes a Deque object and adds each of its elements to the back of self
        :param other: A Deque object
        """

        for e in other.items:
            self.push_back(e)

    def drop_between(self, start, end):
        """
        Deletes elements from the Deque that are within the range [start, end)
        :param start: indicates the first position of the range
        :param end: indicates the last position of the range(does not drop this element)
        """

        # Checks for invalid ranges
        if start < 0 or end > len(self) or start >= end:
            raise IndexError()

        # Deletes elements in range start to end
        i = start
        while i != end:
            del self.items[start]
            i += 1

    def count_if(self, criteria):
        """
        counts how many elements of the Deque satisfy the criteria
        :param criteria: a bool function that takes an element of the Deque
        and returns true if that element matches the criteria and false otherwise
        """

        i = 0
        for e in self.items:
            if criteria(e):
                i += 1
        return i

    # provided functions

    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))
