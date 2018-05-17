import graph

def depth_first_search_recursive(start, graph, visited, count):
    visited.append(start)
    for destionation, weight in graph[start]:
        if destionation not in visited:
            visited.append(depth_first_search_recursive(destionation, graph, visited, count))
        elif destionation in visited:
            count.append(False)

def detect_cycle_in_graph(graph, start):
    visited = []
    count = []
    depth_first_search_recursive(start, graph, visited, count)
    if len(count) != 0 and count[0] == False:
        print("\n Cycle print in Graph \n")
    else:
        print("\n Cycle not present in Graph \n")

def coloring_node(color, node, g):
    if color == 'RED':
        g[node] = 'BLUE'
    else:
        g[node] = 'RED'

def best_first_search(start, graph):
    visited = []
    g = {}
    for source in graph:
        g[source] = None
    queue = [start]
    visited.append(start)
    g[start] = 'RED'
    while len(queue) != 0:
        source = queue.pop(0)
        for nbr, weight in graph[source]:
            if nbr not in visited and g[nbr] != g[source]:
                coloring_node(g[source], nbr, g)
                queue.append(nbr)
                visited.append(nbr)
            elif g[nbr] == g[source]:
                return False
    print("\n Best First Search Result \n {}\n".format(visited))


def detect_bipartile_graph(graph, start):
    if best_first_search(start, graph) is False:
        print("\n Graph is not bipartile \n")
    else:
        print("\n Graph is bipartile \n")


"""
# Example having Cycle graph
# l = [(0,1,5),(0,2,5),(1,2,5),(2,0,5),(2,3,5),(3,3,5)]

# Example DAG Graph
# l = [(1, 2, 5), (1, 3, 5), (2, 4, 5), (2, 5, 5), (3, 6, 5), (4, 7, 5), (5, 7, 5), (6, 5, 5), (6, 7, 5)]

# Not-Bipartile Graph
l = [(1, 2, 5), (2, 3, 5), (3, 4, 5), (4, 5, 5)]

# Bipartile Graph
# l =[(1,2,5),(2,3,5),(3,4,5),(4,5,5),(5,6,5),(6,1,5)]
t = graph_theory.graph.Create_Graph(l, directed=True)
detect_cycle_in_graph(t.graph, 1)

detect_bipartile_graph(t.graph, 1)
"""