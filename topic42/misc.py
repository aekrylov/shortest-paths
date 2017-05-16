import heapq
from math import inf

from topic42.node import Edge, MarkedNode


def _edge_list(node, edges) -> None:
    outs = node.outs
    node.outs = []

    for node_to, w in outs:
        edges.append(Edge(node, node_to, w))
        _edge_list(node_to, edges)


def to_edge_list(nodes) -> [Edge]:
    """
    Returns a list of Edge objects for a graph.
    Each node is visited at least once, each edge is visited only once
    
    time complexity: Theta(|V| + |E|) 
    
    :param nodes: list of nodes 
    :return: list of all edges
    """
    edges = []

    outs_dict = dict()
    for node in nodes:
        outs_dict[node] = node.outs

    for node in nodes:
        _edge_list(node, edges)

    for node in nodes:
        node.outs = outs_dict[node]

    return edges


def to_weight_matrix(nodes):
    """
    Computes weight matrix for a graph.
    
    time complexity: Theta(|V| + |E|)
    space complexity: Theta(|V|^2)
    
    :param nodes: set of nodes
    :type nodes: Node
    :return: matrix w. w[i][j] is a weight of edge between node i and node j, or math.inf if there's no such edge
    """
    w = []
    n = len(nodes)

    for i in range(n):
        w.append([inf]*n)

    for node in nodes:
        w[node.i][node.i] = 0
        for node_to, weight in node:
            w[node.i][node_to.i] = weight

    return w


class PriorityQueue(object):
    """Priority queue based on heap, capable of inserting a new node with
    desired priority, updating the priority of an existing node and deleting
    an abitrary node while keeping invariant"""

    REMOVED = MarkedNode(-1)

    def __init__(self, heap=None):
        """if 'heap' is not empty, make sure it's heapified"""

        if heap is None:
            heap = []

        self.size = len(heap)

        heapq.heapify(heap)
        self.heap = heap
        self.entry_finder = dict({i[-1]: i for i in heap})

    def put(self, node, priority=0):
        """'entry_finder' bookkeeps all valid entries, which are bonded in
        'heap'. Changing an entry in either leads to changes in both."""

        if node in self.entry_finder:
            self.delete(node)
        entry = [priority, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap, entry)
        self.size += 1

    def delete(self, node):
        """Instead of breaking invariant by direct removal of an entry, mark
        the entry as "REMOVED" in 'heap' and remove it from 'entry_finder'.
        Logic in 'pop()' properly takes care of the deleted nodes."""

        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED
        self.size -= 1
        return entry[0]

    def get(self):
        """Any popped node marked by "REMOVED" does not return, the deleted
        nodes might be popped or still in heap, either case is fine."""

        while self.heap:
            priority, node = heapq.heappop(self.heap)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                self.size -= 1
                return node
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return self.size == 0
