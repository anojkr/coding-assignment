import heapq
from graph_theory import heap


def length(u, v, graph):
    for t in graph[u]:
        if t[0] == v:
            return t[1]


def print_result(dist, parent, name):
    print("\n Result single source shortest path using {} \n{} \n{}\n".format(name, dist, parent))

def relax_operation(Q, alt, source, nbr, dist, prev):
        if alt < dist[nbr[0]]:
            index = Q.index([dist[nbr[0]], nbr[0]])
            dist[nbr[0]] = alt
            prev[nbr[0]] = source[1]
            heap.decrease_key(Q, index + 1, alt)  # here index pass as parameter with +1 because heap implemented with starting index 1.

#Dijstra only work with positive edge weight
def Dijkstra(graph, source):
    dist = {}
    prev = {}
    dist[source] = 0
    Q = []
    for v in graph:
        if v != source:
            dist[v] = 1000
            prev[v] = None
        Q.append([dist[v], v])
    heapq.heapify(Q)
    while len(Q) != 0:
        u = heapq.heappop(Q)
        for nbr in graph[u[1]]:
            alt = dist[u[1]] + length(u[1], nbr[0], graph)
            relax_operation(Q, alt, u, nbr, dist, prev )
    print_result(dist, prev, 'Dijkstra')
    return dist, prev

#Bellamford is used to detect it there exist a negative edge weight cycle
def bellam_ford(graph, source):
        dist = {}
        prev = {}
        dist[source] = 0
        Q = []
        for v in graph:
            if v != source:
                dist[v] = 1000
                prev[v] = None
            Q.append([dist[v], v])
        heapq.heapify(Q)
        k = list(graph.keys())
        temp = k.pop()
        for u in k:
            for v in graph[u]:
                alt = dist[u] + length(u, v[0], graph)
                if alt < dist[v[0]]:
                    dist[v[0]] = alt
                    prev[v[0]] = u 
        for nbr in graph[temp]:
            alt = dist[u] + length(u, v[0], graph)
            if alt <= dist[v[0]]:
                print("Bellam Ford Fail")
                return False
        print_result(dist, prev, 'BellamFord')
        return dist, prev