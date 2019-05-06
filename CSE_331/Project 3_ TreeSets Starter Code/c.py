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
        self.root = None
        self.comp = comp
        self.length = 0

    def __len__(self):
        """
        Counts the number of elements in the tree
        :return: The number of elements in the tree
        """
        return self.length

    def height(self):
        """
        Finds the height of the tree
        :return: The height of the tree
        """
        # -1 if the tree is empty
        if self.root is None:
            return -1
        return self.root.height

    def insert(self, item):
        """
        Inserts the item into the tree
        :param item:
        :return: If the operation was successful
        """

        if self.root is None:
            self.root = TreeNode(item)
            self.length += 1
            return True
        return self.root.add_node(self.comp, item, self, self.root)

    def remove(self, item):
        """
        Removes the item from the tree
        :param item:
        :return: If the operation was successful
        """
        if self.root is None:
            return False
        if self.length == 1:
            self.length = 0
            self.root = None
            return True
        return self.root.del_node(self.comp, item, self, self.root)

    def __contains__(self, item):
        """
        Checks if the item is in the tree
        :param item:
        :return: if the item was in the tree
        """
        if self.root is None:
            return False
        return self.root.find(self.comp, item)

    def first(self):
        """
        Finds the minimum item of the tree
        :return:
        """
        # tree is empty
        if self.root is None:
            raise KeyError
        return self.root.find_min().data

    def last(self):
        """
        Finds the maximum item of the tree
        :return:
        """
        # tree is empty
        if self.root is None:
            raise KeyError
        return self.root.find_max().data

    def clear(self):
        """
        Empties the tree
        :return:
        """
        self.root = None
        self.length = 0

    def __iter__(self):
        """
        Does an in-order traversal of the tree
        :return: an iterator for the tree
        """
        if self.root is None:
            return iter([])
        return self.root.__iter__()

    def is_disjoint(self, other):
        """
        Check if two TreeSet is disjoint
        :param other: A TreeSet object
        :return: True if the sets have no elements in common
        """
        # iterate through self's items
        for item in self:
            # if other contains any of them, return false
            if other.__contains__(item):
                return False
        # return true since other did not contain any shared items
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
        :return:
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
        self.height = 0
        # added stuff below

    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self.data
        if self.right is not None:
            yield from self.right

    def count(self):
        """
        Counts the number of nodes starting from the given node
        :return: Number of nodes
        """
        if self.left is None:
            # No right or left
            if self.right is None:
                return 1
            # There is a right node
            return 1 + self.right.count()
        # There is a left node but no right node
        if self.right is None:
            return 1 + self.left.count()
        # There is a left and right node
        return 1 + self.left.count() + self.right.count()

    def add_node(self, comp, item, tree, parent):
        """
        Add a node starting from the self node
        """

        # Keeps track of if an item was ever inserted to a child
        inserted = False

        # item should go on the left
        if comp(self.data, item) > 0:
            # update info since found the right spot
            if self.left is None:
                self.left = TreeNode(item)
                tree.length += 1
                self.height += 1
                return True
            else:
                # recursively call and update whether inserted is true
                inserted = self.left.add_node(comp, item, tree, self)
                # update this node's height (recursively is done upwards)
                self.update_height()
                # rebalance the tree
                if not self.is_balanced():
                    # left, left case
                    if comp(self.left.data, item) > 0:
                        parent.set_child(comp, self.left)
                        # update the root if needed
                        if self is tree.root:
                            tree.root = self.left
                        self.rotate_right()
                    # left, right case
                    else:
                        temp = self.left
                        self.set_child(comp, self.left.right)
                        temp.rotate_left()
                        parent.set_child(comp, self.left)
                        # update the root if needed
                        if self is tree.root:
                            tree.root = self.left
                        self.rotate_right()
                return inserted
        # item should go on the right
        elif comp(self.data, item) < 0:
            # found the right spot, update information and return true
            if self.right is None:
                self.right = TreeNode(item)
                tree.length += 1
                self.height += 1
                return True
            else:
                # same as left side cases
                inserted = self.right.add_node(comp, item, tree, self)
                self.update_height()
                if not self.is_balanced():
                    # right, right case
                    if comp(self.right.data, item) < 0:
                        parent.set_child(comp, self.right)
                        # update root if needed
                        if self is tree.root:
                            tree.root = self.right
                        self.rotate_left()
                    # right, left case
                    else:
                        temp = self.right
                        self.set_child(comp, self.right.left)
                        temp.rotate_right()
                        parent.set_child(comp, self.right)
                        # update root if needed
                        if self is tree.root:
                            tree.root = self.right
                        self.rotate_left()
                return inserted
        # item is already in the tree
        else:
            return False

    def del_node(self, comp, item, tree, parent):

        # keeps track of if an item was deleted
        deleted = False

        # found the node to delete
        if not comp(item, self.data):
            case = self.del_case()
            # if this node is the root
            if self is tree.root:
                self.del_two_child(comp)
            # 0 children case
            elif not case:
                self.del_no_child(comp, parent)
            # 1 child case
            elif case == 1:
                # figure out where the child is
                if self.left is not None:
                    child = self.left
                else:
                    child = self.right
                self.del_one_child(comp, parent, child)
            # 2 children case
            else:
                self.del_two_child(comp)
            tree.length -= 1
            return True
        # the node should be on the left
        elif comp(self.data, item) > 0:
            # it is not in the tree
            if self.left is None:
                return False
            deleted = self.left.del_node(comp, item, tree, self)
            self.update_height()
        else:
            if self.right is None:
                return False
            deleted = self.right.del_node(comp, item, tree, self)
            self.update_height()

        # check for balance
        if not self.is_balanced():
            # right case
            if self.get_right_height() - self.get_left_height() > 0:
                # right, right case
                if self.right.get_right_height() - self.right.get_left_height() > 0:
                    parent.set_child(comp, self.right)
                    # update root if needed
                    if self is tree.root:
                        tree.root = self.right
                    self.rotate_left()
                # right, left case
                else:
                    temp = self.right
                    self.set_child(comp, self.right.left)
                    temp.rotate_right()
                    parent.set_child(comp, self.right)
                    # update root if needed
                    if self is tree.root:
                        tree.root = self.right
                    self.rotate_left()
            # left case
            else:
                # left, left case
                if self.left.get_left_height() - self.left.get_right_height() > 0:
                    parent.set_child(comp, self.left)
                    # update the root if needed
                    if self is tree.root:
                        tree.root = self.left
                    self.rotate_right()
                # left, right case
                else:
                    temp = self.left
                    self.set_child(comp, self.left.right)
                    temp.rotate_left()
                    parent.set_child(comp, self.left)
                    # update the root if needed
                    if self is tree.root:
                        tree.root = self.left
                    self.rotate_right()

        return deleted

    def del_case(self):
        if self.left is None:
            # 0 children
            if self.right is None:
                return 0
            # one child (right)
            else:
                return 1
        # one child (left)
        if self.right is None:
            return 1
        # two children
        return 2

    def del_no_child(self, comp, parent):
        # on the parent's left side
        if comp(parent.data, self.data) > 0:
            parent.left = None
        # on the parent's right side
        else:
            parent.right = None

    def del_one_child(self, comp, parent, child):
        # on the parent's left side
        if comp(parent.data, self.data) > 0:
            parent.left = child
        else:
            parent.right = child

    def del_two_child(self, comp):
        # this is to cover the case where you delete the root
        if self.right is not None:
            # holds the smallest successor node
            temp = self.right.find_min()
            temp_parent = self.right.find_min_parent()

            # take the data of smallest successor
            self.data = temp.data

            # find how many children the temp has
            case = temp.del_case()

            # 0 children
            if not case:
                if temp_parent is not None:
                    temp.del_no_child(comp, temp_parent)
                else:
                    temp.del_no_child(comp, self)
            else:
                if temp.right is None:
                    temp_child = temp.left
                else:
                    temp_child = temp.right
                # this node is the parent
                if temp_parent is None:
                    temp.del_one_child(comp, self, temp_child)
                else:
                    temp.del_one_child(comp, temp_parent, temp_child)

        # the mirror of the other case
        else:
            temp = self.left.find_max()
            temp_parent = self.left.find_max_parent()

            self.data = temp.data

            # find how many children the temp has
            case = temp.del_case()

            # 0 children
            if not case:
                if temp_parent is not None:
                    temp.del_no_child(comp, temp_parent)
                else:
                    temp.del_no_child(comp, self)
            else:
                if temp.right is None:
                    temp_child = temp.left
                else:
                    temp_child = temp.right
                    # this node is the parent
                if temp_parent is None:
                    temp.del_one_child(comp, self, temp_child)
                else:
                    temp.del_one_child(comp, temp_parent, temp_child)

    def set_child(self, comp, child):
        # child goes on the left
        if comp(self.data, child.data) > 0:
            self.left = child
        # child goes on the right
        else:
            self.right = child

    def get_left_height(self):
        if self.left is None:
            return -1
        return self.left.height

    def get_right_height(self):
        if self.right is None:
            return -1
        return self.right.height

    def update_height(self):
        self.height = 1 + max(self.get_left_height(), self.get_right_height())

    def rotate_right(self):
        temp = self.left.right
        self.left.right = self
        # this is to temporary store in order to calculate height
        temp2 = self.left
        self.left = temp
        # update the height of new root and its right child
        self.update_height()
        temp2.update_height()

    def rotate_left(self):
        temp = self.right.left
        self.right.left = self
        # this is to temporary store in order to calculate height
        temp2 = self.right
        self.right = temp
        # update the height of new root and its right child
        self.update_height()
        temp2.update_height()

    def find(self, comp, item):
        # Item should be to the left
        if comp(self.data, item) > 0:
            # Item does not exist
            if self.left is None:
                return False
            # Search in left branch
            else:
                return self.left.find(comp, item)
        # Item should be on the right
        elif comp(self.data, item) < 0:
            # Item does not exist
            if self.right is None:
                return False
            # Search in right branch
            else:
                return self.right.find(comp, item)
        else:
            return True

    def height(self):
        if self.left is None:
            # is a leaf node
            if self.right is None:
                return 0
            # count height of existing right side
            else:
                return 1 + self.right.height()
        # left side exists but right side does not
        if self.right is None:
            return 1 + self.left.height()
        # left and right both exist, use the max
        return 1 + max(self.left.height(), self.right.height())

    def is_balanced(self):
        if self.left is None:
            # left and right are both empty
            if self.right is None:
                return True
            # right is not empty but left is
            else:
                return self.right.height < 1
        # left side exists but right does not
        if self.right is None:
            return self.left.height < 1
        # left and right both exist, check the difference
        return abs(self.left.height - self.right.height) < 2

    def is_tree_balanced(self):
        if self.left is None:
            if self.right is None:
                return True
            else:
                return self.right.is_balanced()
        if self.right is None:
            return self.left.is_balanced()
        return self.left.is_balanced and self.right.is_balanced

    def find_min(self):
        if self.left is None:
            return self
        return self.left.find_min()

    def find_min_parent(self):
        if self.left is None:
            return None
        if self.left.left is None:
            return self
        return self.left.find_min_parent()

    def find_max(self):
        if self.right is None:
            return self
        return self.right.find_max()

    def find_max_parent(self):
        if self.right is None:
            return None
        if self.right.right is None:
            return self
        return self.right.find_max_parent()


def natural_order(x, y):
    return x - y




