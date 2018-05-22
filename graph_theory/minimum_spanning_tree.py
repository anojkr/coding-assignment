import heapq
import heap


class MST:

    def convert_edge_to_graph_form(self, list, directed=False):
        self.graph = dict()
        l = list.copy()
        if directed == False:
            for source, destination, weight in list:
                l.append((destination, source, weight))
        for source, destination, weight in l:
            self.graph[source] = []
        [self.graph[source].append((destination, weight)) for source, destination, weight in l ]

    def convert_graph_to_edges_form(self, graph):
        r = []
        for source in graph:
            for destination, weight in graph[source]:
                r.append((source, destination, weight))
        return r

    def cost_length(self, source, destination, graph):
        for des, weight in graph[source]:
            if des == destination:
                return weight

    def print_mst_node(self, dict, edge_weight, mst):
        keys = sorted(dict.keys())
        print("\nPrism algo to find Minimum spanning tree \n")
        print("Miniumum MST Cost is {}\n".format(mst))
        for d in keys:
            print("{}-->{} = {}".format(dict[d], d, edge_weight[d]))

    def prims(self, graph, start, directed=False):
        mst = 0
        key = {}  # Vertice - edge_weight btw parent/source to chid current node and parent of current node
        parent = {}

        for source in graph:
            key[source] = 1000
            parent[source] = None
        key[start] = 0

        Q = []  # heap
        for x in key:
            Q.append([key[x], x])
        heapq.heapify(Q)

        while len(Q) != 0:
            u = heapq.heappop(Q)
            source = u[1]
            for v in graph[source]:
                destination = v[0]
                cost = self.cost_length(source, destination, graph)
                if [key[destination], destination] in Q and cost < key[destination]:
                    parent[destination] = source  # set parent of current node
                    idx = Q.index([key[destination], destination])
                    key[destination] = cost  # set key value for node
                    # for decrease key always give idx+1
                    Q = heap.decrease_key(Q, idx + 1,
                                          cost)  # here index pass as parameter with +1 because heap implemented with starting index 1.
            mst = mst + u[0]
        self.print_mst_node(parent, key, mst)
        return mst











