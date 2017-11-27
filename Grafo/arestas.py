import aresta as ar
#import vertice as vta

class arestas(object):
    def __init__(self):
        self.listArestas = {}
        self.qtde = 0

    def addAresta(self, v1, v2, ClassV2, peso, info=[]):
        retorno = self.listArestas[v2] = ar.aresta(v1, v2, ClassV2, peso, info)
        if retorno == None:
            return False
        self.qtde += 1
        return True

    def buscaAresta(self, v2):
        if v2 in self.listArestas.keys():
            return self.listArestas[v2]
        return None

    def getListClassArestas(self):
        retorno = []
        for key, valor in self.listArestas.items():
            retorno.append( valor )
        return retorno

    def getListClassVertArestas(self):
        retorno = []
        for key, aresta in self.listArestas.items():
            retorno.append( aresta.getClassDest() )
        return retorno


'''
ars = arestas()

ars.addAresta('a','b',vta.vertice('b',0))

ars.addAresta('a','c',vta.vertice('c',0))

ars.addAresta('a','d',vta.vertice('d',0))

print(ars.getListClassArestas())

print(ars.buscaAresta('c'))
'''
