from topic42.node import MarkedNode
from topic42.algos import dijkstra_heap, floyd_warshall, ford_bellman

if __name__ == '__main__':
    node = MarkedNode(1)
    node2 = MarkedNode(2)
    node3 = MarkedNode(3)

    node.add_out(node2, 5)
    node.add_out(node2, 10)
    node.add_out(node3, 4)
    node2.add_out(node, -4)
    print(node)

    n = 100
    nodes = [MarkedNode(i) for i in range(n)]