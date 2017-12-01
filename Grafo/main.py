from grafo import grafo
import random

if __name__ == '__main__':
    g = grafo()
    #for i in range(100000):
    #    g.addAresta(str(random.randrange(1000)), str(random.randrange(500)))
    g.load_nodes('amigos.txt')
    print("Insercao concluida")
    print("Quantidade de vertices inseridos: {}".format(g.getQtdeVertices()))
    print("Quantidade de arestas existentes: {}".format(g.getQtdeArestas()))

    #me = g.getVertices()[0].getRot()
    #print("\nVertice analisado: {}".format(me))
    g.analises_BFS()
