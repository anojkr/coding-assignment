class Graph:

    def __init__(self, list, directed=False):
        self.graph = dict()
        l = list.copy()
        if directed == False:
            for k in list:
                l.append((k[1], k[0], k[2]))
        for k in l:
            self.graph[k[0]] = []
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
    """cost = [[0, 9, 12, 0, 0, 0, 0, 0, 0], [9, 0, 8, 4, 7, 0, 0, 0, 0], [12, 8, 0, 0, 5, 2, 0, 0],
            [0, 4, 0, 0, 2, 0, 10, 0, 0], [0, 7, 5, 2, 0, 11, 2, 0, 0], [0, 0, 2, 0, 11, 0, 0, 4, 0],
            [0, 0, 0, 10, 2, 0, 0, 4, 3], [0, 0, 0, 0, 0, 4, 4, 0, 13], [0, 0, 0, 0, 0, 0, 3, 13, 0]]"""
    # Graph example
    #http://nptel.ac.in/courses/106103069/Module_8/mst.htm

    x = Graph(l, directed=False)

    visited = []
    from graph_theory import traversal
    b = traversal.Traversal()
    b.best_first_search(1,x.graph)
    b.depth_first_search_recursive(1, x.graph, visited)
    print("Depth First Search Result\n",format(visited))

    from graph_theory.single_shortest_path import Dijkstra
    Dijkstra(x.graph, 1)

    from graph_theory.minimum_spanning_tree import MST
    a = MST()
    a.prism(x.graph, 1)
