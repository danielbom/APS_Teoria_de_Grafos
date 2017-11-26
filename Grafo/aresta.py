
class aresta(object):
    def __init__(self, fonte, dest, ClassDest, info=[]):
        if ClassDest.getRot() != dest:
            print("ClassDest deve corresponder com o destino")
            return None
        self.classDest = ClassDest
        self.destino = dest
        self.fonte = fonte
        self.info = info

    def print(self):
        print("{} -> {}".format(self.fonte, self.destino))

    def getFont(self):
        return self.fonte
    def getDest(self):
        return self.destino
    def getClassDest(self):
        return self.classDest
    def getInfo(self):
        return self.info

'''
a = aresta('a', 'b', vt.vertice('b',0))

print(a.getFont())

print(a.getDest())

print(a.getClassDest())

print(a.getInfo())

print(a.getClassDest().getRot())

print(a.getClassDest().getId())

print(a.getClassDest().getInfo())
      
'''
