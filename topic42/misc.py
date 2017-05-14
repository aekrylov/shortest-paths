from math import inf

from topic42.node import Edge


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
        for node_to, weight in node:
            w[node.i][node_to.i] = weight

    return w