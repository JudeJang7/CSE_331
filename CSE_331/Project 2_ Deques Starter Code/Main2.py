#!/usr/bin/python3

from Deque import Deque


def main(filename):

    import itertools
    deque = Deque()
    for i in range(0, 10):
        deque.push_back(i)

    for (i, j) in itertools.zip_longest(range(0, 10), deque):
        print("i", i)
        print("j", j)
        # self.assertEqual(i, j)

    # for i in deque.items:
    #     print(i)


if __name__ == '__main__':
    main('example.txt')