class Traversal:
	
	def best_first_search(self, start, graph):
		visited = []
		queue = []
		queue.append(start)
		visited.append(start)
		while len(queue) != 0:
			v = queue.pop(0)
			for nbr in graph[v]:
				if nbr[0] not in visited:
					queue.append(nbr[0])
					visited.append(nbr[0])
		print(visited)

	def depth_first_search_recursive(self, start, graph, visited):
		visited.append(start)
		for nbr in graph[start]:
			if nbr[0] not in visited:
				visited.append(self.depth_first_search_recursive(nbr[0], graph, visited))

