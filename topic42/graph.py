from topic42.node import MarkedNode as mnode
from random import randint


class Graph:

    nodes = []
    edges_factor = 0.2
    max_weight = 999

    def __iter__(self):
        return self.nodes.__iter__()

    def __init__(self, vertices_number):
        edges_number = int(vertices_number ** 2 * self.edges_factor)
        edges_count = 0

        # empty graph generation
        for i in range(vertices_number):
            self.nodes.append(mnode(i))

        # edges adding
        for i in range(edges_number):
            while True:
                out_node_index = randint(0, vertices_number-1)
                to_node_index = randint(0, vertices_number-1)
                if self.nodes[out_node_index].add_out(to_node_index, randint(0, self.max_weight)):
                    edges_count += 1
                    break

        print(edges_count)
