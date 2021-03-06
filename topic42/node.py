import math


class Node:

    def __init__(self, i) -> None:
        self.outs = set()
        self.i = i

    def add_out(self, node_to, w) -> bool:
        conn = Connection(node_to, w)
        if conn in self.outs:
            return False

        self.outs.add(conn)
        return True

    def __eq__(self, o: object) -> bool:
        return self.i == o.i

    def __hash__(self) -> int:
        return self.i

    def __iter__(self):
        return self.outs.__iter__()


class MarkedNode(Node):

    visited = False
    d = math.inf

    def __init__(self, i) -> None:
        super().__init__(i)

    def __lt__(self, other):
        return self.d < other.d

    @classmethod
    def from_node(cls, node, d=None):
        dijkstra_node = MarkedNode(node.i)
        dijkstra_node.outs = node.outs
        if d is not None:
            dijkstra_node.d = d

        return dijkstra_node


class Connection:

    def __init__(self, node_to, weight):
        self.node_to = node_to
        self.weight = weight

    def __iter__(self):
        yield self.node_to
        yield self.weight

    def __eq__(self, other):
        return self.node_to == other.node_to

    def __hash__(self) -> int:
        return self.node_to.__hash__()


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight
