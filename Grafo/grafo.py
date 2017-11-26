import vertice as vt
import vertices as vts
import aresta as ar
import arestas as ars
import fila as fl
import pilha as pl
import math
import random

class grafo(object):
    def __init__(self):
        self.vertices = vts.vertices()
        self.maxId = 0
        self.tempo = 0

    def addVertice(self, rotulo, info=[]):
        result = self.vertices.addVertice(rotulo, self.maxId , info)
        if result != None :
            self.maxId += 1
            return result
        return None
    def addAresta(self, v1, v2, info=[]):
        if type(v1) != type("") or type(v2) != type(""):
            print("Rotulos devem ser do tipo string")
            return False
        ClassV1 = self.addVertice(v1)
        ClassV2 = self.addVertice(v2)

        if ClassV1 == None:
            ClassV1 = self.vertices.buscaVertice(v1)

        if ClassV2 != None:
            ClassV1.addAresta(v1, v2, ClassV2, info)

        return True
        
    def print(self):
        self.vertices.print()

    def BFS(self, inicio):
        if type(inicio) != type(""):
            return None
        self.vertices.setInfoVerts(v1=None, info=['b', math.inf, None])
        
        v0 = self.vertices.buscaVertice(inicio)
        if v0 == None:
            self.vertices.setInfoVerts(None)
            print("Entrada invalida")
            return None
        v0.setInfo(['c', 0, None])
        
        fila = fl.fila()
        fila.enfileira( v0 )
        if fila.vazia():
            self.vertices.setInfoVerts(None)
            return None
        
        print("BFS iniciada")
        while not fila.vazia():
            u = fila.desenfileira()
            for v in u.getListClassVertArestas():
                #print(v)
                infoV = v.getInfo()
                if infoV[0] == 'b':
                    v.setInfo(['c', u.getInfo()[1]+1, u.getRot()])
                    fila.enfileira( v )

        print("BSF concluída")
        #self.print()
        
    def DFS(self, inicio=None):
        if inicio != None and type(inicio) != type(""):
            return None
        self.vertices.setInfoVerts(v1=None, info=['b', None, math.inf, math.inf])
        
        Vertices = self.vertices.getVerts()
        if inicio != None:
            u = self.vertices.buscaVertice(inicio)
            if u == None:
                u = Vertices[0]
                Vertices.pop(0)
            else:
                Vertices.remove(u)
        else:
            u = Vertices[0]
            Vertices.pop(0)

        self.tempo = 0
        while len(Vertices) != 0:
            if u.getInfo()[0] == 'b':
                self.DFS_Visit(Vertices, u)
            if len(Vertices) != 0:
                u = Vertices[0]
                Vertices.pop(0)
        self.print()
        print("DFS concluida")

    def DFS_Visit(self, Vertices, u):
        self.tempo += 1
        infoU = u.getInfo()
        u.setInfo(['c', infoU[1], self.tempo, infoU[3]])
        
        for v in u.getListClassVertArestas():
            infoV = v.getInfo()
            if infoV[0] == 'b':
                v.setInfo([infoV[0],u.getRot(),infoV[2],infoV[3]])
                Vertices.remove(v)
                self.DFS_Visit(Vertices, v)
        self.tempo += 1
        infoU = u.getInfo()
        u.setInfo(['p', infoU[1],infoU[2], self.tempo])
        
    def DFS_Khan(self):
        retorno = []
        self.vertices.setInfoVerts(v1=None, info=['b', None, math.inf, math.inf])
        Vertices = self.vertices.getVerts()

        u = Vertices[0]
        self.tempo = 0
        while len(Vertices) != 0:
            print(u.getInfo()[0])
            if u.getInfo()[0] == 'b':
                self.DFS_Khan_Visit(Vertices, u, retorno)
            if len(Vertices) != 0:
                u = Vertices[0]
                Vertices.pop(0)
        return retorno
        
    def DFS_Khan_Visit(self, Vertices, u, retorno):
        infoU = u.getInfo()
        u.setInfo(['c', infoU[1], self.tempo, infoU[3]])
        
        for v in u.getListClassVertArestas():
            infoV = v.getInfo()
            if infoV[0] == 'b':
                v.setInfo([infoV[0],u.getRot(),infoV[2],infoV[3]])
                Vertices.remove(v)
                self.DFS_Visit(Vertices, v)
        self.tempo += 1
        infoU = u.getInfo()
        u.setInfo(['p', infoU[1],infoU[2], self.tempo])
        retorno.append(u)
        print(retorno)
        
    def Khan(self):
        print(self.DFS_Khan())
            


g = grafo()



# Grafo denso
'''
# Desordenado
for i in range(1000000):
    g.addAresta(str(random.randrange(50)),str(random.randrange(60)))
print("Insercao concluida")
# Se der sorte é possivel acontecer aki tambem o q acontece no semi ordenado
'''
'''
# Semi ordenado
for i in range(1000):
    g.addAresta(str(i), str(i+1))
print("Insercao concluida")

# Para DFS recursiva, com 10000 elementos neste modo, alcança
# a profundidade maxima da recursao e retorna um erro
'''

# Grafo simples
g.addAresta('a', 'b')
g.addAresta('a', 'c')
g.addAresta('a', 'd')
g.addAresta('b', 'f')
g.addAresta('f', 'h')
g.addAresta('h', 'i')
g.addAresta('i', 'k')
g.addAresta('k', 'a')

#g.print()

#g.DFS('a')

g.Khan()

'''
    def DFS_(self, inicio=None):
        if inicio != None and type(inicio) != type(""):
            return None
        self.vertices.setInfoVerts(v1=None, info=['b', None, math.inf, math.inf])
        
        Vertices = self.vertices.getVerts()

        if inicio != None:
            u = self.vertices.buscaVertice(inicio)
            if u == None:
                u = Vertices[0]
                Vertices.pop(0)
            else:
                Vertices.remove(u)
        else:
            u = Vertices[0]
            Vertices.pop(0)

        pilha = pl.pilha()
        pilha.empilha(u)
        qtdeV = 0
        while not pilha.vazia():
            infoU = u.getInfo()
            if infoU[0] == 'b':
                qtdeV += 1
                u.setInfo([ 'c', infoU[1], self.tempo, infoU[3] ])
                for v in u.getListClassVertArestas():
                    infoV = v.getInfo()
                    if infoV[0] == 'b':
                        qtdeV += 1
                        v.setInfo([infoU[0], u.getRot(), self.tempo, infoU[3]])
                        pilha.empilha(v):
                    else if infoV[0] == 'c':
                        u = pilha.desempilha()
                infoU = u.getInfo()
                u.setInfo([ 'p', infoU[1], infoU[2] , self.tempo ])
'''
