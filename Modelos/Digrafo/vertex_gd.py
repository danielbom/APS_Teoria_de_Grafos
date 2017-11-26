class Vertex(object):
	def __init__(self, node):
		self.id = node
		self.adjacency = []

	def __str__(self):
		return '<Node {}> => {}'.format(
			self.id, self.adjacency)
