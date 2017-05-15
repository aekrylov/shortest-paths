from topic42.graph import Graph
from topic42.algos import dijkstra_heap, floyd_warshall, ford_bellman
import time

orders = [i for i in range(100, 2001, 100)]

dijkstra_results = open('results/dijkstra.txt', 'w')
floyd_warshall_results = open('results/floyd_warshall.txt', 'w')
ford_bellman_results = open('results/ford_bellman.txt', 'w')

for order in orders:
    print('Processing order %s' % order)
    graph = Graph(order)

    time_before = time.clock()
    for i in range(order):
        dijkstra_heap(graph.nodes, graph.nodes[i])
    dijkstra_results.write(str(order) + ' ' + str(time.clock() - time_before) + '\n')

    # time_before = time.clock()
    # for i in range(order):
    #     ford_bellman(graph.nodes, graph.nodes[i])
    # ford_bellman_results.write(str(order) + ' ' + str(time.clock() - time_before) + '\n')

    # time_before = time.clock()
    # floyd_warshall(graph.nodes)
    # floyd_warshall_results.write(str(order) + ' ' + str(time.clock() - time_before) + '\n')
