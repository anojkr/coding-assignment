class Create_Graph:

    def __init__(self, list, directed=False):
        self.graph = dict()
        l = list.copy()
        if directed == False:
            for k in list:
                l.append((k[1], k[0], k[2]))
        for k in l:
            self.graph[k[0]] = []
            self.graph[k[1]] = []
        [self.graph[k[0]].append((k[1], k[2])) for k in l]
        print(self.graph)

    def add_edges_to_nodes(self, list, directed=False):
        l = list.copy()
        if directed == False:
            for k in list:
                l.append((k[1], k[0], k[2]))
        for k in l:
            if k[0] not in self.graph:
                self.graph[k[0]] = []
            elif k[1] not in self.graph:
                self.graph[k[1]] = []
        [self.graph[k[0]].append((k[1], k[2])) for k in l]
        print(self.graph)


if __name__ == '__main__':
    # l= [(1,2,2),(1,4,6),(2,3,3),(2,4,8),(2,5,5),(3,5,7),(4,5,9)]
    # cost = [[0, 2, 0, 6, 0],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]
    l = [(1, 2, 9), (1, 3, 12), (2, 3, 8), (2, 4, 4), (2, 5, 7), (3, 5, 5), (3, 6, 2), (4, 5, 2), (4, 7, 10),
         (5, 6, 11), (5, 7, 2), (6, 8, 4), (7, 8, 4), (7, 9, 3), (8, 9, 13)]
    #l = [(1, 2, 5), (1, 3, 5), (2, 4, 5), (2, 5, 5), (3, 6, 5), (4, 7, 5), (5, 7, 5), (6, 5, 5), (6, 7, 5)]
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

    visited = []
    from graph_theory import traversal

    b = traversal.Traversal()
    b.best_first_search(1, x.graph)
    b.depth_first_search_recursive(1, x.graph, visited)
    print("Depth First Search Result\n", format(visited))

    from graph_theory.minimum_spanning_tree import MST

    a = MST()
    a.prism(x.graph, 1)

    from graph_theory.single_shortest_path import Dijkstra

    Dijkstra(x.graph, 1)

    from graph_theory.single_shortest_path import bellam_ford

    bellam_ford(x.graph, 1)

    from graph_theory.detect_cycle import detect_cycle_in_graph
    detect_cycle_in_graph(x.graph, 1)
