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

    def cost_length(self, u, v, graph):
        for t in graph[u]:
            if t[0] == v:
                return t[1]

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
                cost = self.cost_length(u[1],v[0], graph)
                if [key[v[0]], v[0]] in Q and cost < key[v[0]]:
                    parent[v[0]] = u[1]  # set parent of current node
                    idx = Q.index([key[v[0]], v[0]])
                    key[v[0]] = cost  # set key value for node
                    # for decrease key always give idx+1
                    Q = heap.decrease_key(Q, idx + 1,
                                          cost)  # here index pass as parameter with +1 because heap implemented with starting index 1.
            mst = mst + u[0]
        self.print_mst_node(parent, key, mst)
        return mst











