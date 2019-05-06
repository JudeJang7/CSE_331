""" This module creates a Graph data structure
    Method used for storing edges was to create a list of all the edges (edge list).
"""

import math


class Graph:
    """
    A weighted graph
    Features path capabilities, minimum weight, bipartite
    """
    def __init__(self, n):

        """
        Constructor
        :param n: Number of vertices
        """

        self.order = n
        self.size = 0

        # You may put any required initialization code here

        self.edges = []

    def insert_edge(self, u, v, w):
        """
        Adds an edge of the given weight between the two vertices
        :param u: starting vertex
        :param v: ending vertex
        :param w: weight of edge
        """

        if u + 1 > self.order or v + 1 > self.order:
            raise IndexError

        else:
            self.size += 1

            for e in self.edges:
                if e[0] == u and e[1] == v:
                    self.size -= 1

            self.edges.append((u, v, w))

    def degree(self, v):
        """
        Calculates the number of edges that intersect the given vertex.
        :param v: vertex
        :return: the number of edges that intersect the given vertex.
        """

        degree = 0
        exists = False

        for e in self.edges:
            if e[0] == v:
                degree += 1
                exists = True
            if e[1] == v:
                degree += 1
                exists = True

        if not exists:
            raise IndexError

        return degree

    def are_connected(self, u, v):
        """
        Checks whether an edge exists between two vertices
        :param v: starting vertex
        :param v: ending vertex
        :return: if vertices are connected
        """

        connected = False

        if u + 1 > self.order or v + 1 > self.order:
            raise IndexError

        else:
            for e in self.edges:
                if e[0] == u and e[1] == v:
                    connected = True
                if e[0] == v and e[1] == u:
                    connected = True

        return connected

    def is_path_valid(self, path):
        """
        Determines whether an edge exists along each step of the path.
        :param path: path between two vertices
        :return: if path is valid
        """

        i = 0
        for _ in path:
            if len(path) == 1:
                return True
            elif i != len(path) - 1:
                if not self.are_connected(path[i], path[i + 1]):
                    return False
            i += 1

        return True

    def edge_weight(self, u, v):
        """
        Finds the weight of an edge between two vertices
        :param u: starting vertex
        :param v: ending vertex
        :return: edge weight
        """

        if self.are_connected(u, v):
            for e in self.edges:
                if e[0] == u and e[1] == v:
                    return e[2]
                if e[0] == v and e[1] == u:
                    return e[2]

        return math.inf

    def path_weight(self, path):
        """
        Finds the total weight of a path (sum of edge weights)
        :param path: path between two vertices
        :return: weight of path
        """

        weight = 0
        i = 0
        for _ in path:
            if len(path) == 1:
                return 0
            elif i != len(path) - 1:
                if path[0] == path[1]:
                    return 0.0
                elif not self.are_connected(path[i], path[i + 1]):
                    return math.inf
                else:
                    for e in self.edges:
                        if (e[0] == path[i] and e[1] == path[i + 1]) or (e[0] == path[i + 1] and e[1] == path[i]):
                            weight += e[2]
            i += 1

        return weight

    def does_path_exist(self, u, v):
        """
        Checks whether a path exists between two vertices
        :param u: starting vertex
        :param v: ending vertex
        :return: if path exists
        """

        paths = []

        if u + 1 > self.order or v + 1 > self.order:
            raise IndexError

        elif u == v:
            return True

        else:
            for e in self.edges:
                if (e[0] == u and e[1] == v) or (e[0] == v and e[1] == u):
                    return True
                if u == e[0]:
                    if e[1] == v:
                        return True
                    else:
                        paths.append([e[0], e[1]])
                if u == e[1]:
                    if e[0] == v:
                        return True
                    else:
                        paths.append([e[0], e[1]])

        paths2 = []
        for f in paths:
            for g in self.edges:
                if f[1] == g[0]:
                    if g[1] == v:
                        return True
                    else:
                        paths2.append([g[0], g[1]])
                if f[0] == g[1]:
                    if g[0] == u:
                        return True
                    else:
                        paths2.append([g[0], g[1]])

        paths3 = []
        for h in paths2:
            for i in self.edges:
                if h[1] == i[0]:
                    if i[1] == v:
                        return True
                    else:
                        paths3.append([i[0], i[1]])
                if h[0] == i[1]:
                    if i[0] == v:
                        return True
                    else:
                        paths3.append([i[0], i[1]])

        for j in paths3:
            for k in self.edges:
                if j[1] == k[0]:
                    if k[1] == v:
                        return True
                if j[0] == k[1]:
                    if k[0] == v:
                        return True

        return False

    def find_min_weight_path(self, u, v):
        """
        Finds a path of minimum weight between two vertices
        :param u: starting vertex
        :param v: ending vertex
        """

        edges = []
        paths = []
        weights = []

        if not self.does_path_exist(u, v):
            raise ValueError

        if u == v:
            return [u, v]

        else:
            for e in self.edges:
                if (e[0] == u and e[1] == v) or (e[0] == v and e[1] == u):
                    return [u, v]
                if u == e[0]:
                    if e[1] == v:
                        return [u, v]
                    else:
                        edges.append([e[0], e[1], e[2]])
                if u == e[1]:
                    if e[0] == v:
                        return [u, v]
                    else:
                        edges.append([e[0], e[1], e[2]])

        for f in edges:
            for g in self.edges:
                if f[1] == g[0]:
                    if g[1] == v:
                        print(f[2] + g[2])
                        paths.append([f[0], f[1], g[1], f[2] + g[2]])
                if f[0] == g[1]:
                    if g[0] == u:
                        print(f[2] + g[2])
                        paths.append([f[0], f[1], g[1], f[2] + g[2]])

        for h in paths:
            weights.append(h[3])

        w = min(weights)
        for i in paths:
            if w == i[3]:
                return[i[0], i[1], i[2]]
        return [u, v]

    def is_bipartite(self):
        """
        Determines if the graph is bipartite
        :return: if graph is bipartite
         """

        v1 = []
        v2 = []

        for e in self.edges:
            v1.append(e[0])
            v2.append(e[1])

        for i in v1:
            count1 = v1.count(i)
            count2 = v2.count(i)
            if count1 > 1:
                return False
            if count2 > 1:
                return False

        for j in v2:
            count3 = v2.count(j)
            count4 = v1.count(j)
            if count3 > 1:
                return False
            if count4 > 1:
                return False

        return True

