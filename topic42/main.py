from topic42.graph import Graph

graph = Graph(10)

for node in graph:
    print(node.i)
    for out in node.outs:
        print(' --- ', out.node_to, out.weight)