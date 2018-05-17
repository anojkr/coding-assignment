import heapq
import heap


def length(u, v, graph):
    for t in graph[u]:
        if t[0] == v:
            return t[1]

def print_result(dist, parent, name):
    print("\n Result single source shortest path using {} \n{} \n{}\n".format(name, dist, parent))

def relax_operation(Q, alt, source, destionation, dist, prev):
        if alt < dist[destionation]:
            index = Q.index([dist[destionation], destionation])
            dist[destionation] = alt
            prev[destionation] = source
            heap.decrease_key(Q, index + 1, alt)  # here index pass as parameter with +1 because heap implemented with starting index 1.

#Dijstra only work with positive edge weight
def Dijkstra(graph, source_node):
    dist = {}
    prev = {}
    dist[source_node] = 0
    Q = []
    for source in graph:
        if source != source_node:
            dist[source] = 1000
            prev[source] = None
        Q.append([dist[source], source])
    heapq.heapify(Q)
    while len(Q) != 0:
        u = heapq.heappop(Q)
        src = u[1] #Source node
        for destionation, weight in graph[src]:
            alt = dist[src] + length(src, destionation, graph)
            relax_operation(Q, alt, src, destionation, dist, prev )
    print_result(dist, prev, 'Dijkstra')
    return dist, prev

#Bellamford is used to detect it there exist a negative edge weight cycle
def bellam_ford(graph, source_node):
        dist = {}
        prev = {}
        dist[source_node] = 0
        Q = []

        for source in graph:
            if source != source_node:
                dist[source] = 1000
                prev[source] = None
            Q.append([dist[source], source])
        heapq.heapify(Q)
        k = list(graph.keys())
        temp = k.pop()

        for src in k: #Here src is source node
            for destionation, weight in graph[src]:
                alt = dist[src] + length(src, destionation, graph)
                if alt < dist[destionation]:
                    dist[destionation] = alt
                    prev[destionation] = src 

        for nbr in graph[temp]:
            alt = dist[src] + length(src, destionation, graph)
            if alt <= dist[destionation]:
                print("Bellam Ford Fail")
                return False

        print_result(dist, prev, 'BellamFord')
        return dist, prev