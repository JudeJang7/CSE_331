""" This module creates a TreeSet class and TreeNode class from scratch.
    A set is used as the data structure for the TreeSet class.
    Strategy used for TreeSet class is based off of AVL Trees.
    If tree is left heavy, do right rotation
    If tree is right heavy, do left rotation
"""


class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """

    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """

        self.comp = comp

        # added stuff below

        self.root = None

    def __len__(self):
        """
        Counts the number of elements in the tree
        :return: number of elements in the tree
        """

        if self.root is None:
            return 0

        return self.root.tree_length()

    def height(self):
        """
        Finds the height of the tree
        :return: the height of the tree
        """

        if self.root is None:
            return -1

        return self.root.tree_height()

    def insert(self, item):
        """
        Inserts the item into the tree
        :param item: item that will be inserted into the tree
        :return: If the operation was successful
        """

        if self.root is None:
            self.root = TreeNode(item)
            return True

        if not self.__contains__(item):
            self.root.tree_insert(item, self.comp)
            return True

        return False

    def remove(self, item):
        """
        Removes the item from the tree
        :param item: item that will be removed from the tree
        :return: If the operation was successful
        """

        if self.root is None:
            return False

        if self.root.data == item and len(self) == 1:
            self.root = None
            return True

        if self.__contains__(item):
            self.root.tree_remove(item, self.comp)
            return True

        return False

    def __contains__(self, item):
        """
        Checks if the item is in the tree
        :param item: item to be checked if in tree
        :return: if the item was in the tree
        """

        if self.root is not None:

            if self.comp(item, self.root.data) == 0:
                return True

            if self.comp(item, self.root.data) != 0:
                return self.root.tree_contains(item, self.comp)

        return False

    def first(self):
        """
        Finds the minimum item of the tree
        :return: minimum item of the tree
        """

        if self.root is None:
            raise KeyError

        for e in self:
            return e

    def last(self):
        """
        Finds the maximum item of the tree
        :return: maximum item of the tree
        """

        if self.root is None:
            raise KeyError

        temp = None

        for e in self:
            temp = e
        return temp

    def clear(self):
        """
        Empties the tree
        :return: empty tree
        """

        self.root = None

    def __iter__(self):
        """
        Does an in-order traversal of the tree
        :return: elements of the tree in-order traversal
        """

        if self.root is None:
            return iter([])

        return iter(self.root)

    def is_disjoint(self, other):
        """
        Check if two TreeSet is disjoint
        :param other: A TreeSet object
        :return: True if the sets have no elements in common
        """

        for e in self:
            if e in other:
                return False

        return True

    # Pre-defined methods

    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))

    def __bool__(self):
        """
        Checks if the tree is non-empty
        :return: if the tree if non-empty
        """
        return not self.is_empty()

    # Helper functions
    # You can add additional functions here


class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """

    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None

        # added stuff below

        self.parent = None

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)

    def tree_length(self):
        """
        Recursively gets the length of the tree
        :return: length of tree
        """

        if self.left is None:
            left_length = 0
        if self.left is not None:
            left_length = self.left.tree_length()

        if self.right is None:
            right_length = 0
        if self.right is not None:
            right_length = self.right.tree_length()

        return 1 + (left_length + right_length)

    def tree_height(self):
        """
        Recursively gets the height of the tree
        :return: height of tree
        """

        if self.left is None:
            left_height = -1
        if self.left is not None:
            left_height = self.left.tree_height()

        if self.right is None:
            right_height = -1
        if self.right is not None:
            right_height = self.right.tree_height()

        return 1 + max(left_height, right_height)

    def tree_insert(self, item, comp):
        """
        Inserts the item into the tree
        :param item: item that will be inserted into the tree
        :param comp: compare function
        """

        if comp(self.data, item) > 0:
            if self.left is None:
                self.left = TreeNode(item)
                self.left.parent = self
            else:
                self.left.tree_insert(item, comp)

        if comp(self.data, item) < 0:
            if self.right is None:
                self.right = TreeNode(item)
                self.right.parent = self
            else:
                self.right.tree_insert(item, comp)

    def tree_remove(self, item, comp):
        """
        Removes the item from the tree
        :param item: item that will be removed from the tree
        :param comp: compare function
        :return: If the operation was successful
        """

        if comp(self.data, item) != 0:
            if comp(self.data, item) > 0:
                if self.left is not None:
                    return self.left.tree_remove(item, comp)

            if comp(self.data, item) < 0:
                if self.right is not None:
                    return self.right.tree_remove(item, comp)

        else:
            if self.left is None and self.right is None and self.parent is not None:
                if self.parent.data < self.data:
                    self.data = None
                    self.parent.right = None
                    return True

                elif self.parent.data > self.data:
                    self.data = None
                    self.parent.left = None
                    return True

                elif self.parent.data == self.data:
                    if self.parent.left and self.parent.left.data == self.data:
                        self.parent.left = None
                        self.data = None
                        return True

                    elif self.parent.right and self.parent.right.data == self.data:
                        self.parent.right = None
                        self.data = None
                        return True

            elif self.left is None and self.right:
                temp = self
                if self.right is not None:
                    temp = self.right

                if temp.left:
                    while temp.left:
                        temp = temp.left

                self.data = temp.data
                self.right.tree_remove(temp.data, comp)

            elif self.right is None and self.left:
                temp = self
                if self.left is not None:
                    temp = self.left

                if temp.right:
                    while temp.right:
                        temp = temp.right

                self.data = temp.data
                self.left.tree_remove(temp.data, comp)

            elif self.left and self.right:
                temp = self
                if self.right is not None:
                    temp = self.right

                if temp.left:
                    while temp.left:
                        temp = temp.left

                self.data = temp.data
                self.right.tree_remove(temp.data, comp)

        return True

    def tree_contains(self, item, comp):
        """
        Checks if the item is in the tree
        :param item: item to be checked if in tree
        :param comp: compare function
        :return: If the operation was successful
        """

        if comp(item, self.data) == 0:
            return True

        if comp(item, self.data) != 0:

            if comp(item, self.data) < 0:
                if self.left is None:
                    return False
                else:
                    return self.left.tree_contains(item, comp)

            if comp(item, self.data) > 0:
                if self.right is None:
                    return False
                else:
                    return self.right.tree_contains(item, comp)

        return False

    def __iter__(self):
        """
        Does an in-order traversal of the tree
        """

        if self.left is not None:
            yield from self.left

        yield self.data

        if self.right is not None:
            yield from self.right
