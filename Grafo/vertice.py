import arestas as ars

class vertice(object):
    def __init__(self, rotulo, id, info=[]):
        self.rotulo = rotulo
        self.id = id
        self.info = info
        self.arestas = ars.arestas()

    def addAresta(self, fonte, dest, ClassDest, peso=1, info=[]):
        return self.arestas.addAresta(fonte, dest, ClassDest, peso, info)

    def getRot(self):
        return self.rotulo
    def getId(self):
        return self.id
    def getInfo(self):
        return self.info
    def getArestas(self):
        return self.arestas.getListClassArestas()
    def getQtdeArestas(self):
        return self.arestas.getQtde()

    def getListClassArestas(self):
        return self.arestas.getListClassArestas()

    def getListClassVertArestas(self):
        return self.arestas.getListClassVertArestas()

    def setInfo(self, info):
        self.info = info
    def setId(self, id):
        self.id = id
    def setRot(self, rotulo):
        self.rotulo = rotulo

    def print(self, x):
        if x == 1:
            print("{}[ {} ]".format(self.rotulo, self.id))
        elif x == 2:
            print("Vertice {}".format(self.rotulo))
            for i in self.arestas.getListClassArestas():
                i.print()
        elif x == 3:
            print("{}  {}".format(self.rotulo, self.info))
