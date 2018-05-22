from collections import defaultdict
from itertools import groupby

class Create_Graph:

    def __init__(self, list_nodes, directed=False):
        self.graph = defaultdict(list)
        l = list_nodes.copy()

        if directed == False:
            self.make_undirected_graph(list_nodes, l)
        self.graph = self.setup_graph(l, self.graph)
        self.print_graph()

    def add_edges_to_nodes(self, list_nodes, graph, directed=False):
        l = list_nodes.copy()
        if directed == False:
            self.make_undirected_graph(list_nodes, l)
        self.setup_graph(l, graph)
        self.print_graph()

    def make_undirected_graph(self, list_nodes, l):
        for source, destionation, weight in list_nodes:
            l.append((destionation, source, weight))
        return l

    def setup_graph(self, l, graph):
        for key, group in groupby(l, lambda x : x[0]):
            for t in group:
                graph[key].append(t[1:])
        return dict(graph)

    def print_graph(self):
        print("\nGraph shown below")
        print("\nSource : [(destination, weight)]\n")
        print("{")
        for t in self.graph.items():
            print("\t {}".format(t))
        print("}")


if __name__ == '__main__':
    # l= [(1,2,2),(1,4,6),(2,3,3),(2,4,8),(2,5,5),(3,5,7),(4,5,9)]
    l = [(1, 2, 9), (1, 3, 12), (2, 3, 8), (2, 4, 4), (2, 5, 7), (3, 5, 5), (3, 6, 2), (4, 5, 2), (4, 7, 10),
         (5, 6, 11), (5, 7, 2), (6, 8, 4), (7, 8, 4), (7, 9, 3), (8, 9, 13)]
    #b = [(1, 2, 5), (1, 3, 5), (2, 4, 5), (2, 5, 5), (3, 6, 5), (4, 7, 5), (5, 7, 5), (6, 5, 5), (6, 7, 5)]
    # Example for bellam ford as -ve edge weight given
    # l = [(1, 2, -1), (1, 3, 4), (2, 3, 3), (2, 4, 2), (2, 5, 2), (4, 2, 1), (4, 3, 5), (5, 4, -3),(3,3,0)]

    """
    
    Notes:
    1. Dijstra only work with positive edge cycle
    2. Bellam ford is used to detect negative edge weight cycle in graph
    3. If graph is directed make parameter directed=True
    4. Input to graph is list of edge weight btw source node to neighbour node
    
    # Graph example
    #http://nptel.ac.in/courses/106103069/Module_8/mst.htm
    
    """
    x = Create_Graph(l, directed=False)
    #x.add_edges_to_nodes(b, x.graph)

    visited = []
    import traversal

    b = traversal.Traversal()
    b.best_first_search(1, x.graph)
    b.depth_first_search_recursive(1, x.graph, visited)
    print("Depth First Search Result\n", format(visited))

    from minimum_spanning_tree import MST
    a = MST()
    a.prims(x.graph, 1)

    from single_shortest_path import Dijkstra, bellam_ford
    Dijkstra(x.graph, 1)
    bellam_ford(x.graph, 1)

    from detect_cycle import detect_cycle_in_graph, detect_bipartile_graph
    detect_cycle_in_graph(x.graph, 1)
    detect_bipartile_graph(x.graph, 1)


