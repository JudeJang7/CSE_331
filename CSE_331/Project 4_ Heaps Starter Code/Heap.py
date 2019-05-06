""" This module creates a Heap data structure
    Overall method used to implement heap is to insert items into a list and then heapify.
    Strategy for find_median is to insert elements into min_heap based on seq,
    call extract k times, k being the length/2, then returning the extracted value of the min_heap.
"""


class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """

    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """

        self.comp = comp

        # Added Members
        self.length = 0
        self.heap = []

    def __len__(self):
        """
        Finds the number of items in the heap
        :return: The size
        """

        return self.length

    def peek(self):
        """
        Finds the item of highest priority
        :return: The item item of highest priority
        """

        if self.is_empty():
            raise IndexError

        else:
            return self.heap[0]

    def insert(self, item):
        """
        Adds the item to the heap
        :param item: An item to insert
        """

        # https://d2l.msu.edu/d2l/le/content/661872/viewContent/7263462/View
        # Insert: Slide 16

        self.heap.append(item)
        i = len(self)
        self.length += 1

        while i > 0 and self.comp(item, self.heap[self.parent(i)]):
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)

        self.heap[i] = item

    def extract(self):
        """
        Removes the item of highest priority
        :return: the item of highest priority
        """

        # https://d2l.msu.edu/d2l/le/content/661872/viewContent/7263462/View
        # Extract: Slide 19

        if self.is_empty():
            raise IndexError

        m = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.length -= 1
        self.heapify(0)
        self.heap.pop()

        return m

    def extend(self, seq):
        """
        Adds all elements from the given sequence to the heap
        :param seq: An iterable sequence
        """

        for e in seq:
            self.heap.append(e)
            self.length += 1

        i = int(len(self)/2)
        while i >= 0:
            self.heapify(i)
            i -= 1

    def replace(self, item):
        """
        Adds the item the to the heap and returns the new highest-priority item
        Faster than insert followed by extract.
        :param item: An item to insert
        :return: The item of highest priority
        """

        self.insert(item)
        return self.extract()

    def clear(self):
        """
        Removes all items from the heap
        """

        self.length = 0
        self.heap = []

    def __iter__(self):
        """
        An iterator for this heap
        :return: An iterator
        """

        for e in self.heap:
            yield e

    # Supplied methods

    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()

    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))

    # Added methods

    @staticmethod
    def parent(i):
        """
        Calculates new index
        :param i: index
        :return: new index
        """

        return (i - 1) // 2

    def heapify(self, i):
        """
        Converts list to a heap
        :param i: index
        """

        # https://d2l.msu.edu/d2l/le/content/661872/viewContent/7263462/View
        # Heapify: Slide 21

        l = i * 2 + 1
        r = i * 2 + 2
        if l < len(self.heap) and self.comp(self.heap[l], self.heap[i]):
            small = l
        else:
            small = i
        if r < len(self.heap) and self.comp(self.heap[r], self.heap[small]):
            small = r
        if small != i:
            self.heap[i], self.heap[small] = self.heap[small], self.heap[i]
            self.heapify(small)

    # Required Non-heap member function


def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """

    # https://d2l.msu.edu/d2l/le/content/661872/viewContent/7263462/View
    # Slide 30

    if not seq:
        raise IndexError
    min_heap = Heap(lambda a, b: a < b)

    for e in seq:
        min_heap.insert(e)

    i = 0
    k = min_heap.length//2

    while i < k:
        min_heap.extract()
        i += 1

    return min_heap.extract()
