import vertice as vt

class vertices(object):
    def __init__(self):
        self.listVerts = {}
        self.qtde = 0

    def addVertice(self, rotulo, id, info=[]):
        if type(rotulo) != type(""):
            print("Rotulo do vertice deve ser do tipo string")
            return None
        if rotulo in self.listVerts.keys():
            return None
        self.listVerts[rotulo] = vt.vertice(rotulo, id, info)
        self.qtde += 1
        return self.listVerts[rotulo]

    def getVerts(self):
        retorno = []
        for key, vertice in self.listVerts.items():
            retorno.append(vertice)
        return retorno

    def getMatrizAdj(self):
        if self.qtde > 1000:
            resp = input("Quantidade de vértices maior que 1000. Deseja continuar? s/n: ")
            if resp.upper() == 'N':
                return None
        matrix = [[0 for x in range(self.qtde)] for y in range(self.qtde)]
        for key, v1 in self.listVerts.items():
            idV1 = v1.getId()
            for v2 in v1.getListClassVertArestas():
                idV2 = v2.getId()
                matrix[idV1][idV2] = 1
        return matrix

    def getMatrizAdjPesos(self):
        if self.qtde > 1000:
            resp = input("Quantidade de vértices maior que 1000. Deseja continuar? s/n: ")
            if resp.upper() == 'N':
                return None
        matrix = [[0 for x in range(self.qtde)] for y in range(self.qtde) ]
        for key, v1 in self.listVerts.items():
            idV1 = v1.getId()
            arestas = v1.getArestas()
            for a in arestas:
                idV2 = a.getClassDest().getId()
                matrix[idV1][idV2] = a.getPeso()
        return matrix

    def getQtdeArestas(self):
        qtde = 0
        for key, i in self.listVerts.items():
            qtde += i.getQtdeArestas()
        return qtde

    def buscaVertice(self, rotulo):
        if rotulo in self.listVerts.keys():
            return self.listVerts[rotulo]
        return None

    def getQtde(self):
        return self.qtde

    def setInfoVerts(self, v1=None, info=[]):
        if type(info) == type(list) and len(info) == 0:
            return False
        if v1 != None:
            self.buscaVertice(v1).setInfo(info)
            return True
        for key, v in self.listVerts.items():
            v.setInfo(info)
        return True

    def print(self, x):
        for key, valor in self.listVerts.items():
            valor.print(x)
