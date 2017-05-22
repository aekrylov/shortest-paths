import math
import time

from topic42.algos import dijkstra_heap, floyd_warshall, ford_bellman, ford_bellman2
from topic42.graph import Graph


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

    outfile.write(str(order) + '\t' + str(len(graph.edges)) + '\t' + str(time.clock() - time_before) + '\n')
    outfile.flush()
    return d


def test_simple_graph(orders):
    # dijkstra_results = open('results/dijkstra.txt', 'w')
    # floyd_warshall_results = open('results/floyd_warshall.txt', 'w')
    # ford_bellman_results = open('results/ford_bellman.txt', 'w')

    for order in orders:
        graph = Graph(order)

        def fb_test(nodes, init_node):
            return ford_bellman2(nodes, graph.edges, init_node)

        d_dijkstra = test_algorithm(graph, dijkstra_heap, dijkstra_results)
        d_bellman = test_algorithm(graph, fb_test, ford_bellman_results)
        d_warshall = test_algorithm(graph, floyd_warshall, floyd_warshall_results, False)

        if d_dijkstra == d_bellman == d_warshall:
            print("OK")
        else:
            print("FAIL")


if __name__ == '__main__':
    # orders = [i for i in range(10000, 10001, 250)]
    orders = [10000]

    dijkstra_results = open('results/10-9/dijkstra.txt', 'a')
    # floyd_warshall_results = open('results/10-9/floyd_warshall.txt', 'w')
    # ford_bellman_results = open('results/10-9/ford_bellman.txt', 'a')

    # test_simple_graph(orders)

    for order in orders:
        graph = Graph(order)
        test_algorithm(graph, dijkstra_heap, dijkstra_results)
        # test_algorithm(graph, floyd_warshall, floyd_warshall_results, False)
        # test_algorithm(graph, ford_bellman, ford_bellman_results)
