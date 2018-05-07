import graph_theory.graph


def depth_first_search_recursive(start, graph, visited):
    visited.append(start)
    for nbr in graph[start]:
        if nbr[0] not in visited:
            visited.append(depth_first_search_recursive(nbr[0], graph, visited))
        elif nbr[0] in visited:
            return False


def detect_cycle_in_graph(graph, start):
    visited = []
    if depth_first_search_recursive(start, graph, visited) is False:
        print("Cycle detected in graph")
    else:
        print("No Cycle detected in graph")


# Example having Cycle graph
# l = [(0,1,5),(0,2,5),(1,2,5),(2,0,5),(2,3,5),(3,3,5)]

# Example DAG Graph
l = [(1, 2, 5), (1, 3, 5), (2, 4, 5), (2, 5, 5), (3, 6, 5), (4, 7, 5), (5, 7, 5), (6, 5, 5), (6, 7, 5)]
# t = graph_theory.graph.Create_Graph(l, directed=True)
# detect_cycle_in_graph(1, t.graph)
