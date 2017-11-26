# -*- coding: cp1252 -*-
from aresta import Arestas
import math
import fila

# Vertice == {rotulo : arestas(rotulo, id)}
class Grafo:
    def __init__(self):
        self.Vertices = {}
        self.num_vertices = 0
        self.id = 1

    def addVertice(self, rotulo, info=None):
        if rotulo not in self.Vertices.keys():
            self.Vertices[rotulo] = [info, Arestas(rotulo=rotulo, id=self.id)]
            self.id += 1
    
    def getInfo(self, de):
        return self.Vertices[de][0]
    
    def setInfo(self, de, info=None):
        self.Vertices[de][0] = info
    
    # info pode ser uma lista de itens( para fazer buscas, entre outras coisas )
    def addAresta(self, de, para, info = {'peso': 1}):
        if de not in self.Vertices.keys():
            self.addVertice(de)
        if para not in self.Vertices.keys():
            self.addVertice(para)

        self.Vertices[de][1].addAresta( para, info )

    
    def BFS(self, de, para=None):
        #self.Vertices[de].setInfoV({'cor' : 'c', 'Du' : 0, 'pred' : None})
        rel = []
        rel.append(0)
        
        for v in self.Vertices:
            self.setInfo(v, ['b',math.inf, None])
        self.setInfo(de, ['c', 0, None])
        
        Q = fila.fila()
        Q.push(de)
        while not Q.vazia():
            u = Q.pop()
            infou = self.getInfo(u)
            rel[infou[1]] += 1
            naoB = 0
                
            for v in self.Vertices[u][1].getArestas():
                infov = self.getInfo(v)
                if infov[0] == 'b':
                    self.setInfo(v, ['c', infou[1]+1, u])
                    Q.push(v)
                else:
                    naoB += 1

            if self.Vertices[u][1].getQtdeArestas() != naoB:
                rel.append(0)
            self.setInfo(u, ['p', infou[1], infou[2]])

        print("Concluido")
        if len(rel) > 1000:
            atua = []
            atua.append(0)
            k = 0
            for i in range(len(rel)):
                atua[k] += rel[i]
                if i % 100 == 0:
                    atua.append(0)
                    k += 1
                    
        print(atua[0:50])
        print(rel[:50])
    
        
    '''       
    def get_arestas_do_vertice(self, rotulo):
        return self.Vertices[rotulo].getInfo() if rotulo in self.Vertices else None

    
    def get_grau_vertice(self, rotulo):
        cont = 0
        if (Type):
            for key, valor in self.Vertices.items():
                if rotulo == key:
                    cont += len(valor[1].keys())
                for aresta in valor[1].keys():
                    if rotulo == aresta:
                        cont += 1
        return cont
    '''
    def print(self):
        for key in self.Vertices.keys():
            print("{} - {}".format(key, self.getInfo(key)))
            #print(self.Vertices[key][1].getArestasInfo())
            
    


g = Grafo()
for i in range(1000000):
    g.addAresta(i, i+1)

print("Concluido")
g.BFS(1)


'''
g = Grafo()

g.addAresta('A', 'B')
g.addAresta('A', 'C')
g.addAresta('B', 'C')
g.addAresta('C', 'D')
g.addAresta('D', 'A')
#g.print()
g.BFS('A')
'''
'''
g.addVertice("A")
g.addVertice("E")
g.print()

g.add_aresta("A", "F")

ar = g.get_arestas_do_vertice("A")
print(ar)

print("\n")
g.printGrafo()
print(g.get_grau_vertice("A"))
'''
