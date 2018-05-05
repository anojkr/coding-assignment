import heapq
from graph_theory import heap


class MST:

    def convert_edge_to_graph_form(self, list, directed=False):
        self.graph = dict()
        l = list.copy()
        if directed == False:
            for k in list:
                l.append((k[1], k[0], k[2]))
        for k in l:
            self.graph[k[0]] = []
        [self.graph[k[0]].append((k[1], k[2])) for k in l]

    def convert_graph_to_edges_form(self, graph):
        r = []
        for t in graph:
            for s in graph[t]:
                r.append((t, s[0], s[1]))
        return r

    def print_mst_node(self, dict, edge_weight, mst):
        keys = sorted(dict.keys())
        print("\nPrism algo to find Minimum spanning tree \n")
        print("Miniumum MST Cost is {}\n".format(mst))
        for d in keys:
            print("{}-->{} = {}".format(dict[d], d, edge_weight[d]))

    def prism(self, graph, start, cost, directed=False):
        mst = 0
        key = {}  # Vertice - edge_weight btw parent/source to chid current node and parent of current node
        parent = {}
        for t in graph:
            key[t] = 1000
            parent[t] = None
        key[start] = 0
        Q = []  # heap
        for x in key:
            Q.append([key[x], x])
        heapq.heapify(Q)
        while len(Q) != 0:
            u = heapq.heappop(Q)
            for v in graph[u[1]]:
                if [key[v[0]], v[0]] in Q and cost[u[1] - 1][v[0] - 1] < key[v[0]]:
                    parent[v[0]] = u[1]  # set parent of current node
                    idx = Q.index([key[v[0]], v[0]])
                    key[v[0]] = cost[u[1] - 1][v[0] - 1]  # set key value for node
                    # for decrease key always give idx+1
                    z = cost[u[1] - 1][v[0] - 1]
                    Q = heap.decrease_key(Q, idx + 1,
                                          z)  # here index pass as parameter with +1 because heap implemented with starting index 1.
            mst = mst + u[0]
        self.print_mst_node(parent, key, mst)
        return mst











