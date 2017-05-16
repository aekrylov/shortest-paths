import math
import time

from topic42.algos import dijkstra_heap, floyd_warshall, ford_bellman2
from topic42.graph import Graph, SparseGraph


def test_algorithm(graph, algo, outfile, iterate=True):
    order = len(graph.nodes)
    time_before = time.clock()

    if iterate:
        d = [[math.inf]*order]*order

        for i in range(order):
            algo(graph.nodes, graph.nodes[i])
            d[i] = [graph.nodes[j].d for j in range(order)]  # fill distances between i and all others

    else:
        d = algo(graph.nodes)

    outfile.write(str(order) + ' ' + str(time.clock() - time_before) + '\n')
    outfile.flush()
    return d


def test_all(graph, dijkstra_results, ford_bellman_results, floyd_warshall_results):
    def fb_test(nodes, init_node):
        return ford_bellman2(nodes, graph.edges, init_node)

    d_dijkstra = test_algorithm(graph, dijkstra_heap, dijkstra_results)
    d_bellman = test_algorithm(graph, fb_test, ford_bellman_results)
    d_warshall = test_algorithm(graph, floyd_warshall, floyd_warshall_results, False)

    if d_dijkstra == d_bellman == d_warshall:
        print("OK")
    else:
        print("FAIL")


def test_simple_graph(orders):
    dijkstra_results = open('results/dijkstra.txt', 'w')
    floyd_warshall_results = open('results/floyd_warshall.txt', 'w')
    ford_bellman_results = open('results/ford_bellman.txt', 'w')

    for order in orders:
        graph = Graph(order)
        test_all(graph, dijkstra_results, ford_bellman_results, floyd_warshall_results)


def test_sparse_graph(orders, powers):
    for power in powers:
        dijkstra_results = open('results/dijkstra_%.1f.txt' % power, 'w')
        floyd_warshall_results = open('results/floyd_warshall_%.1f.txt' % power, 'w')
        ford_bellman_results = open('results/ford_bellman_%.1f.txt' % power, 'w')

        for order in orders:
            graph = SparseGraph(order, power)
            test_all(graph, dijkstra_results, ford_bellman_results, floyd_warshall_results)


if __name__ == '__main__':
    orders = [i for i in range(100, 501, 100)]
    powers = [x/10 for x in range(11, 20, 2)]

    test_sparse_graph(orders, powers)