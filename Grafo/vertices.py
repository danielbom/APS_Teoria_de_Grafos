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
            #print("Vertice '{}' ja existe".format(rotulo))
            return None
        self.listVerts[rotulo] = vt.vertice(rotulo, id, info)
        self.qtde += 1
        return self.listVerts[rotulo]

    def getVerts(self):
        retorno = []
        for key, vertice in self.listVerts.items():
            retorno.append(vertice)
        return retorno

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

    def print(self):
        for key, valor in self.listVerts.items():
            valor.printZ()
