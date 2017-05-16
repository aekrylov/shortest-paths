import math
from .misc import PriorityQueue

from topic42.misc import to_weight_matrix, to_edge_list
from topic42.node import MarkedNode


def reset_marks(nodes):
    for node in nodes:
        node.visited = False
        node.d = math.inf


def dijkstra_heap(nodes, node_init):
    """
    Dijkstra algorithm using binary heap. Computes shortest paths between node_init and all the connected nodes
    TODO compute path
    
    time complexity: O(|E| * log(|V|))
    
    :param nodes: list of all nodes 
    :param node_init:
     :type node_init: MarkedNode
    :return: 
    """
    reset_marks(nodes)

    node_init.d = 0

    q = PriorityQueue()
    q.put(node_init, 0)

    while not q.empty():
        top = q.get()
        if top.visited:
            continue
        top.visited = True

        for node_to, w in top:
            if node_to.visited:
                continue

            d_new = top.d + w
            if d_new < node_to.d:
                # one node can be put multiple times, with different distances.
                # If the node was visited once, it will not be visited anymore
                node_to.d = d_new
                q.put(node_to, d_new)


def floyd_warshall(nodes):
    """
    Computes min distances between all pairs of nodes in a graph.
    
    time complexity: Theta(|V|^3)
    space complexity: Theta(|V|^2)
    
    :param nodes: list of all nodes
    :return: matrix of minimum distances 
    """
    d = to_weight_matrix(nodes)
    n = len(nodes)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d


def ford_bellman(nodes, node_init):
    """
    Computes shortest paths between node_init and all other nodes.
    This version first computes edge list from graph, thus sometimes ford_bellman2 will be much more efficient
    
    time complexity: Theta(|V| * |E|)
    
    :param nodes: list of all nodes
     :type nodes: [DijkstraNode]
    :param node_init: start node 
    :return: None 
    """
    edges = to_edge_list(nodes)

    return ford_bellman2(nodes, edges, node_init)


def ford_bellman2(nodes, edges, node_init):
    """
    Computes shortest paths between node_init and all other nodes.

    :param nodes: 
    :param edges: 
    :param node_init: 
    :return: 
    """
    n = len(nodes)
    reset_marks(nodes)

    node_init.d = 0

    for i in range(n):
        for edge in edges:
            edge.second.d = min(edge.second.d, edge.first.d + edge.weight)
