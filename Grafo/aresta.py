
class Arestas(object):
    def __init__(self, rotulo, id):
        self.arestas = {}
        self.rotulo = rotulo
        self.id = id
        self.info = []
    def add_vizinho(self, para, info=[1]):
        if para not in self.arestas.keys():
            self.arestas[para] = info
    def getInfo(self):
        return [self.id, self.arestas, self.info]
