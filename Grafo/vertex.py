class Vertex:
	def __init__(self, node):
		self.id = node
		self.adjacent = {}

	def __str__(self):
		return 'Vertex {} -> {}'.format(
			self.id, [key for key, value in self.adjacent.items()])

	def add_neighbor(self, neighbor, weight=0):
		self.adjacent[neighbor] = weight

	def get_connections(self):
		return self.adjacent.keys()

	def get_weight(self, neighbor):
		return self.adjacent[neighbor]

	def get_degree(self):
		return len(self.adjacent)
