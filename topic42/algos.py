import math
from queue import PriorityQueue

from topic42.misc import to_weight_matrix, to_edge_list
from topic42.node import MarkedNode


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
    q = PriorityQueue()
    q.put(node_init)

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
                q.put(node_to)


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
    Computes shortest paths between node_init and all other nodes
    
    time complexity: Theta(|V| * |E|)
    
    :param nodes: list of all nodes
     :type nodes: [DijkstraNode]
    :param node_init: start node 
    :return: None 
    """
    edges = to_edge_list(nodes)

    n = len(nodes)
    for node in nodes:
        node.d = math.inf

    node_init.d = 0

    for i in range(n):
        for edge in edges:
            edge.second.d = min(edge.second.d, edge.first.d + edge.weight)