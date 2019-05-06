""" This module implement a dynamic program that solves the longest increasing subsequence problem.
    Method used for computing LIS is by using a binary search with an upper and lower bound.
"""


def verify_subseq(seq, subseq):
    """
    Determines whether one sequence is a subsequence of another
    :param seq: sequence
    :param subseq: subsequence
    :return: whether one sequence is a subsequence of another
    """

    # https://stackoverflow.com/questions/24017363/how-to-test-if-one-string-is-a-subsequence-of-another

    it = iter(seq)
    return all(c in it for c in subseq)


def verify_increasing(seq):
    """
    Determines whether a sequence is in increasing order
    :param seq: sequence
    :return: whether sequence is in increasing order
    """

    # https://stackoverflow.com/questions/24577688/compare-current-item-to-next-item-in-a-python-list

    for i, j in enumerate(seq[:-1]):
        if j >= seq[i + 1]:
            return False
    return True


def find_lis(seq):
    """
    Finds the longest increasing subsequence of the given sequence
    :param seq: sequence
    :return: longest increasing subsequence
    """

    # https://rosettacode.org/wiki/Longest_increasing_subsequence#Python:_O.28nlogn.29_Method_from_Wikipedia.27s_LIS_Article.5B1.5D

    l = len(seq)
    previous = [0] * l
    minimum = [0] * (l + 1)
    length = 0
    for i in range(l):
        low = 1
        high = length
        while low <= high:
            mid = (low + high) // 2
            if seq[minimum[mid]] < seq[i]:
                low = mid + 1
            else:
                high = mid - 1

        new = low
        previous[i] = minimum[new - 1]
        minimum[new] = i

        if new > length:
            length = new

    s = []
    k = minimum[length]
    for i in range(length - 1, -1, -1):
        s.append(seq[k])
        k = previous[k]
    return s[::-1]
