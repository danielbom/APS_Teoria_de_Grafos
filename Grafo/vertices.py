import vertice as vt
import operator

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

    def buscaVertice(self, rotulo):
        if rotulo in self.listVerts.keys():
            return self.listVerts[rotulo]
        return None

    def getQtde(self):
        return self.qtde

    def getVerts(self):
        return [ v for v in self.listVerts.values()]

    def getArestas(self):
        return [v.getArestas() for v in self.listVerts.values()]

    def getArestasSort(self):
        arestas = self.getArestas()
        temp = []
        for i in arestas:
            for j in i:
                temp.append(j)
        temp.sort(key=operator.attrgetter('peso'))
        return temp

    def getMatrizAdj(self):
        if self.qtde > 1000:
            resp = input("Quantidade de vértices maior que 1000. Deseja continuar? s/n: ")
            if resp.upper() == 'N':
                return None
        matrix = [[0 for x in range(self.qtde)] for y in range(self.qtde)]
        for v1 in self.listVerts.values():
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
        for v1 in self.listVerts.values():
            idV1 = v1.getId()
            arestas = v1.getArestas()
            for a in arestas:
                idV2 = a.getClassDest().getId()
                matrix[idV1][idV2] = a.getPeso()
        return matrix

    def getQtdeArestas(self):
        qtde = 0
        for i in self.listVerts.values():
            qtde += i.getQtdeArestas()
        return qtde

    def getSorvedouros(self):
        retorno = []
        for i in self.listVerts.values():
            if i.getQtdeArestas() == 0:
                retorno.append(i)
        return retorno

    def getFontes(self):
        vertices = {i.getRot(): i for i in self.getVerts()}
        remova = set()
        for v1 in vertices.values():
            for v2 in v1.getListClassArestas():
                if v2.getDest() in vertices:
                    remova.add(v2.getDest())
        for i in remova:
            vertices.pop(i)
        return [v for v in vertices.values()]

    def setInfoVerts(self, v1=None, info=[]):
        if type(info) == type(list) and len(info) == 0:
            return False
        if v1 != None:
            self.buscaVertice(v1).setInfo(info)
            return True
        for v in self.listVerts.values():
            v.setInfo(info)
        return True

    def setInfoArestas(self, info):
        for v in self.listVerts.values():
            v.setInfoArestas(info)
    
    def print(self, x):
        for key, valor in self.listVerts.items():
            valor.print(x)
