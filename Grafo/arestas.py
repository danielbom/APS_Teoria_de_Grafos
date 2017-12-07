import aresta as ar
#import vertice as vta

class arestas(object):
    def __init__(self):
        self.listArestas = {}
        self.qtde = 0

    def addAresta(self, v1, v2, ClassV2, peso, info=[]):
        self.listArestas[v2] = ar.aresta(v1, v2, ClassV2, peso, info)
        q = self.qtde
        self.qtde = len(self.listArestas)
        if q == self.qtde:
            return False
        return True

    def buscaAresta(self, v2):
        if v2 in self.listArestas.keys():
            return self.listArestas[v2]
        return None

    def getListClassArestas(self):
        return [v for v in self.listArestas.values()]

    def getListClassVertArestas(self):
        return [a.getClassDest() for a in self.listArestas.values()]

    def getQtde(self):
        return self.qtde

    def setInfoArestas(self, info):
        for a in self.listArestas.values():
            a.setInfo(info)