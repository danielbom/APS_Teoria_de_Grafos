from Grafo.vertex import Vertex


class Graph:
	def __init__(self):
		self.vert_dict = {}
		self.num_vertices = 0

	def __iter__(self):
		return iter(self.vert_dict.values())

	def add_vertex(self, node):
		new_vertex = Vertex(node)
		self.vert_dict[node] = new_vertex
		self.num_vertices += 1

	def get_vertex(self, node):
		return self.vert_dict[node] if node in self.vert_dict else None

	def add_edge(self, frm, to, cost=0):
		if frm not in self.vert_dict:
			self.add_vertex(frm)
		if to not in self.vert_dict:
			self.add_vertex(to)

		self.vert_dict[frm].add_neighbor(self.add_vertex(to), cost)
		self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

	def get_vertices(self):
		return self.vert_dict.keys()

	def get_vertex_degree(self, node):
		count = 0
		for key, value in self.vert_dict.items():
			if node in [i.id for i in value.adjacent.keys()]:
				count += 1
		return count
