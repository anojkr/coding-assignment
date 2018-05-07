import graph_theory.graph

def depth_first_search_recursive(start, graph, visited, count):
    visited.append(start)
    for nbr in graph[start]:
        if nbr[0] not in visited:
            visited.append(depth_first_search_recursive(nbr[0], graph, visited, count))
        elif nbr[0] in visited:
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
    for k in graph:
        g[k] = None
    queue = [start]
    visited.append(start)
    g[start] = 'RED'
    while len(queue) != 0:
        v = queue.pop(0)
        for nbr in graph[v]:
            if nbr[0] not in visited and g[nbr[0]] != g[v]:
                coloring_node(g[v], nbr[0], g)
                queue.append(nbr[0])
                visited.append(nbr[0])
            elif g[nbr[0]] == g[v]:
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