
"""
Application of Breadth first search

1.  It can be used to find minimum cost spanning trees in undirected/ same weighted graph.

2.  It can be used to check graph is bi-partile or not

Application of Depth first search

1.  It can be used to detect cycle in directed/undirected
    graph. {If there is back-edge in graph then cycle exist in graph}

2.  For unweighted/Same weighted grah dfs can be used to find
    minimum cos spanning tree_theory and all pair shortest path {path is measured
    in term of number of edges btw source node and destination node.}

3.  Dfs can be used to find topological sorting in Directed Acyclic Graph.

4.  It can be used to detech graph is bi-partile of not.

"""

class Traversal:

    def best_first_search(self, start, graph):
        visited = []
        queue = [start]
        visited.append(start)
        while len(queue) != 0:
            source = queue.pop(0)
            for destination, weight in graph[source]:
                if destination not in visited:
                    queue.append(destination)
                    visited.append(destination)
        print("\nBest First Search Result\n {}\n".format(visited))

    def depth_first_search_recursive(self, start, graph, visited):
        visited.append(start)
        for destination, weight in graph[start]:
            if destination not in visited:
                visited.append(self.depth_first_search_recursive(destination, graph, visited))
