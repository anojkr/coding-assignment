import heapq
from graph_theory import heap


def length(u, v, graph):
    for t in graph[u]:
        if t[0] == v:
            return t[1]


def print_result(dist, parent):
    print("\n Result single source shortest path using Dijkstra")
    print(dist)
    print(parent)


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
            if alt < dist[nbr[0]]:
                index = Q.index([dist[nbr[0]], nbr[0]])
                dist[nbr[0]] = alt
                prev[nbr[0]] = u[1]
                heap.decrease_key(Q, index + 1,
                                  alt)  # here index pass as parameter with +1 because heap implemented with starting index 1.
    print_result(dist, prev)
    return dist, prev
