from Digrafo.vertex_gd import Vertex


class Graph(object):
	def __init__(self):
		self.vertices = {}

	def add_edge(self, frm, to):
		if frm not in self.vertices:
			self.vertices[frm] = Vertex(frm)
		if to not in self.vertices:
			self.vertices[to] = Vertex(to)

		self.vertices[frm].adjacency.append({'to': Vertex(to)})

	def remove_edge(self, frm, to):
		for i in range(0, len(self.vertices[frm].adjacency)):
			if to in self.vertices[frm].adjacency[i].values():
				self.vertices[frm].adjacency.pop(i)
				self.vertices[frm].degree[1] -= 1  # out
				self.vertices[to].degree[0] -= 1   # in
				return  # SUPONDO QUE SÓ PODE HAVER UMA ARESTA PARA O UM VERTICE
