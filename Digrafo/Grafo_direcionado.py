# -*- coding: cp1252 -*-
from aresta import Arestas

Type = True # True não instancia Arestas, false sim
# Entre true e false, p/ 1 000 000, true é mais rapido para adicionar arestas

class Grafo:
    def __init__(self):
        self.Vertices = {}
        self.num_vertices = 0
        self.id = 1

    def add_vertice(self, rotulo):
        if rotulo not in self.Vertices:
            #print("{} - Vertice ainda nao existe".format(rotulo))
            if (Type):
                self.Vertices[rotulo] = [self.id, {}]
            else:
                self.Vertices[rotulo] = Arestas(rotulo, self.id)
            self.id += 1
        else:
            #print("Vertice ja existe")
            pass

    # info pode ser uma lista de itens( para fazer buscas, entre outras coisas )
    def add_aresta(self, de, para, info=1):
        if de not in self.Vertices.keys():
            self.add_vertice(de)
        if para not in self.Vertices.keys():
            self.add_vertice(para)

        if (Type):
            self.Vertices[de][1][para] = info
            ### sem direcao, entao
            #self.Vertices[para][1][de] = info
        else:
            self.Vertices[de].add_vizinho( para, info )
            ### sem direcao, entao
            #self.Vertices[para].add_vizinho( de, info )
            
    def get_arestas_do_vertice(self, rotulo):
        if(Type):
            return self.Vertices[rotulo] if rotulo in self.Vertices else None
        else:
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
    
    def printGrafo(self):
        for i in self.Vertices.keys():
            if(type):
                print("{} - {}".format(i,self.Vertices[i]))
            else:
                tmp = self.Vertices[i].getInfo()
                print("{} {} - {}".format(i,tmp[0], tmp[1]))
                if len(tmp[2]) > 0:
                    print(tmp[2])
            
    

'''
g = Grafo()
for i in range(1000000):
    #print(i)
    g.add_vertice(i)

g.add_aresta(900000, 6, 10)
print("Concluido")
'''


g = Grafo()

g.add_aresta('A', 'B')
g.add_aresta('B', 'C')
g.add_aresta('C', 'D')
g.add_aresta('D', 'A')

g.add_vertice("A")
g.add_vertice("E")

g.add_aresta("A", "F")

ar = g.get_arestas_do_vertice("A")
print(ar)

print("\n")
g.printGrafo()
print(g.get_grau_vertice("A"))

