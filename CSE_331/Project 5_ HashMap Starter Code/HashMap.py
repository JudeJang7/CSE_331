""" This module creates a Hash Map data structure
    Method used for handling collisions is to use linear probing.
    If a slot is taken, go to the next available slot and insert the key, value pair.
"""


class HashMap:
    """
    A hash map
    Associative data structure that pairs key and value items together
    """
    def __init__(self, load_factor=1.00):

        # You may change the default maximum load factor
        self.max_load_factor = load_factor

        # Other initialization code can go here
        self.map = []
        self.size = 0

    def __len__(self):
        return self.size

    @staticmethod
    def buckets():
        """
        Counts the number of slots that map has for storing items
        :return: Number of slots that map has for storing items
        """
        return 0

    @staticmethod
    def load():
        """
        Computes the load factor: the average number of items per slot
        :return: Load factor
        """
        return 0.0

    def __contains__(self, key):
        for e in self.map:
            if e[0] == key:
                return True
        return False

    def __getitem__(self, key):
        """
        Determines which value item is associated with a given key
        :param: key: Key to get associated value
        :return: Value associated with given key
        """

        if not self.__contains__(key):
            raise KeyError(key)

        i = 0
        for e in self.map:
            if e[0] != key:
                i += 1
            if e[0] == key:
                return e[1]

        return False

    def __setitem__(self, key, value):

        if not self.__contains__(key):
            self.map.append([key, value])
            self.size += 1

        if self.__contains__(key):
            for e in self.map:
                if e[0] == key:
                    e[1] = value

    def __delitem__(self, key):

        if not self.__contains__(key):
            raise KeyError(key)

        i = 0
        for e in self.map:
            if e[0] != key:
                i += 1
            if e[0] == key:
                self.map.remove(self.map[i])
                self.size -= 1

    def __iter__(self):
        # while False:
        #     yield (key, value) # Yield key-value pairs

        for e in self.map:
            yield e

    def clear(self):
        """
        Removes all associations from the map
        """
        self.map = []
        self.size = 0

    def keys(self):
        """
        Returns a set of the keys contained in the map
        :return: Set of keys
        """

        keys = set()

        for e in self.map:
            keys.add(e[0])
        return keys

    # supplied methods

    def __repr__(self):
        """
        A string representation of this map
        :return: A string representing this map
        """
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        """
        Checks if there are items in the map
        :return True if the map is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks that there are no items in the map
        :return: True if there are no bindings
        """
        return len(self) == 0

    # Helper functions can go here


# Required Function
def year_count(input_hashmap):
    """
    Function to count the number of students born in the given year
    :input: A HashMap of student name and its birth year
    :returns: A HashMap of the year and the number of students born in that year
    """

    hash_map = HashMap()
    keys = set()

    for e in input_hashmap:
        keys.add(e[1])

    for k in keys:
        i = 0
        for e in input_hashmap:
            if e[1] == k:
                i += 1
                hash_map.__setitem__(e[1], i)

    return hash_map
