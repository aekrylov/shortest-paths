from random import randrange

from topic42.misc import to_edge_list
from topic42.node import MarkedNode as mnode


class Graph:

    edges_factor = 10/9
    max_weight = 999

    def E(self, N):
        return int(N ** self.edges_factor)

    def __iter__(self):
        return self.nodes.__iter__()

    def __init__(self, N):
        edges_number = self.E(N)
        self.nodes = []

        # empty graph generation
        for i in range(N):
            self.nodes.append(mnode(i))

        # edges adding
        for i in range(edges_number):
            while True:
                out_node_index = randrange(0, N)
                to_node_index = randrange(0, N)
                if out_node_index != to_node_index and \
                        self.nodes[out_node_index].add_out(self.nodes[to_node_index],
                                                           randrange(0, self.max_weight)):
                    break

        self.edges = to_edge_list(self.nodes)
        print("Created graph with %d nodes and %d edges" % (N, edges_number))

class SparseGraph(Graph):

    def __init__(self, N, k):
        self.k = k
        super().__init__(N)

    def E(self, N):
        return int(N ** self.k)