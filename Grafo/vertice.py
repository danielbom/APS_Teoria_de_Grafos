import arestas as ars

class vertice(object):
    def __init__(self, rotulo, id, info=[]):
        self.rotulo = rotulo
        self.id = id
        self.info = info
        self.arestas = ars.arestas()

    def addAresta(self, fonte, dest, ClassDest, info=[]):
        return self.arestas.addAresta(fonte, dest, ClassDest, info)

    def printX(self):
        print("{}[ {} ]".format(self.rotulo, self.id))

    def printY(self):
        print("Vertice {}".format(self.rotulo))
        for i in self.arestas.getListClassArestas():
            i.print()

    def printZ(self):
        print("{}  {}".format(self.rotulo, self.info))
    
    def getRot(self):
        return self.rotulo
    def getId(self):
        return self.id
    def getInfo(self):
        return self.info
    
    def getListClassVertArestas(self):
        return self.arestas.getListClassVertArestas()

    def setInfo(self, info):
        self.info = info
    def setId(self, id):
        self.id = id
    def setRot(self, rotulo):
        self.rotulo = rotulo

'''
v = vertice("a", 0)

print(v.getRot())

print(v.getId())

print(v.getInfo())


print(type(vertice('a',0)))
'''

