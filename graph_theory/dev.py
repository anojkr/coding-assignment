# d = {'R': [('M', 1)], 'M': [('Q', 2), ('N', 3), ('R', 1)], 'N': [('Q', 4), ('O', 5), ('M', 3)], 'O': [('P', 5), ('N', 5)], 'P': [('Q', 4), ('O', 5)], 'Q': [('M', 2), ('N', 4), ('P', 4)]}
# cost = [[0,3,0,0,2,1],[3,0,5,0,4,0],[0,5,0,5,0,0],[0,0,5,0,4,0],[2,4,0,4,0,0],[1,0,0,0,0,0]]

#d = {1: [(2, 2), (4, 6)], 2: [(3, 3), (4, 8), (5, 5), (1, 2)], 3: [(5, 7), (2, 3)], 4: [(5, 9), (1, 6), (2, 8)], 5: [(2, 5), (3, 7), (4, 9)]}
#cost = [[0, 2, 0, 6, 0],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]

#d = {2: [(3, 5), (5, 3), (1, 6)], 1: [(2, 6), (3, 1), (4, 5)], 3: [(4, 5), (5, 6), (6, 4), (1, 1), (2, 5)],4: [(6, 2), (1, 5), (3, 5)], 6: [(3, 4), (4, 2), (5, 6)], 5: [(6, 6), (2, 3), (3, 6)]}
#cost = [[0, 6, 1, 5, 0, 0], [6, 0, 5, 0, 3, 0], [1, 5, 0, 5, 6, 4], [5, 0, 5, 0, 0, 2], [0, 3, 6, 0, 0, 6],[0, 0, 4, 2, 6, 0]]

d = {1: [(2, 9), (3, 12)], 2: [(3, 8), (4, 4), (5, 7), (1, 9)], 3: [(5, 5), (6, 2), (1, 12), (2, 8)], 4: [(5, 2), (7, 10), (2, 4)], 5: [(6, 11), (7, 2), (2, 7), (3, 5), (4, 2)], 6: [(8, 4), (3, 2), (5, 11)], 7: [(8, 4), (9, 3), (4, 10), (5, 2)], 8: [(9, 13), (6, 4), (7, 4)], 9: [(7, 3), (8, 13)]}
cost = [[0,9,12,0,0,0,0,0,0],[9,0,8,4,7,0,0,0,0],[12,8,0,0,5,2,0,0],[0,4,0,0,2,0,10,0,0],[0,7,5,2,0,11,2,0,0],[0,0,2,0,11,0,0,4,0],[0,0,0,10,2,0,0,4,3],[0,0,0,0,0,4,4,0,13],[0,0,0,0,0,0,3,13,0]]
import heapq
import numpy
from graph_theory import heap

def print_mst_node(dict, edge_weight):
    keys = sorted(dict.keys())
    for d in keys:
        print("{}-->{} = {}".format(dict[d], d, edge_weight[d]))


def weighted_adjmatrix(adjlist, nodes):
    '''Returns a (weighted) adjacency matrix as a NumPy array.'''
    matrix = []
    for node in nodes:
        weights = {endnode:int(weight)
                   for w in adjlist.get(node, {})
                   for endnode, weight in w.items()}
        matrix.append([weights.get(endnode, 0) for endnode in nodes])
    matrix = numpy.array(matrix)
    return matrix + matrix.transpose()


def prism(graph, start, cost):
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
    print(Q)
    while len(Q) != 0:
        u = heapq.heappop(Q)
        print(Q)
        print("pop element from heap {}".format(u))
        for v in graph[u[1]]:
            #print(v) # Here U[0] keyvalue, U[1]-- source node , v[0] destionation node, v[1] edge weight btw source and destination
            #print("Curren heap status {}".format(Q))
            #print("Source Node - {}  its neigbour {}".format(u[1], v[0]))
            #print(key)
            #print("check value present in heap or not {}".format([key[v[0]], v[0]]))
            if [key[v[0]], v[0]] in Q and cost[u[1]-1][v[0]-1] < key[v[0]]:
                parent[v[0]]  =   u[1] #set parent of current node
                print("inside check value present in heap or not{}".format([key[v[0]], v[0]]))
                idx = Q.index([key[v[0]], v[0]])
                key[v[0]] = cost[u[1]-1][v[0]-1] #set key value for node
                #for decrease key always give idx+1
                z = cost[u[1]-1][v[0]-1]
                print("idx {}".format(idx+1))
                print("value of key in cost matrix {}".format(z))
                Q = heap.decrease_key(Q, idx+1, z)
                print("After decrease key heap status - {}".format(Q))
                #print("\n")
        mst = mst + u[0]
        print(mst)
    print_mst_node(parent, key)
    return mst

#prism(d, 1, cost)
k = sorted(d.keys())
print(weighted_adjmatrix(d,k))