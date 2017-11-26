
class Arestas(object):
    def __init__(self, rotulo, id):
        self.arestas = {}
        self.rotulo = rotulo
        self.id = id
        
    def addAresta(self, para, infoA = {'peso': 1}):
        if para not in self.arestas.keys():
            self.arestas[para] = infoA
            
    def getInfo(self, para):
        return self.arestas[para]
    def getQtdeArestas(self):
        return len(self.arestas)
    
    def getArestas(self):
        return self.arestas
    def getArestasInfo(self):
        arInf = []
        for a in self.arestas:
            arInf.append([a, self.arestas[a]])
        return arInf
    
    def getId(self):
        return self.id
        
    def setId(self, id):
        self.id = id
        

'''
ar = Arestas("A", 1)
ar.addInfoV( {'BST': 0} )
print(ar.getInfoV())
'''
