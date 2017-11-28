import vertice as vt
import vertices as vts
import aresta as ar
import arestas as ars
import fila as fl
import pilha as pl
import math
import random


class grafo(object):
    def __init__(self, filename):
        self.vertices = vts.vertices()
        self.maxId = 0  # indicador de quantidade e controle para uso do FloydWarshall
        self.tempo = 0
        self.load_nodes(filename)

    def load_nodes(self, filename):
        with open(filename) as file:
            content = [line.strip() for line in file.readlines()]
            friends = list(map(lambda friend: tuple(friend.split(' -> ')), content))
            for frm, to in friends:
                self.addAresta(frm, to)

    def addVertice(self, rotulo, info=[]):
        result = self.vertices.addVertice(rotulo, self.maxId , info)
        if result != None :
            self.maxId += 1
            return result
        return None

    def getQntdeVertice(self):
        return self.maxId

    def addAresta(self, v1, v2, peso=1, info=[]):
        if type(v1) != type("") or type(v2) != type(""):
            print("Rotulos devem ser do tipo string")
            return False
        ClassV1 = self.addVertice(v1)
        ClassV2 = self.addVertice(v2)

        if ClassV1 == None:
            ClassV1 = self.vertices.buscaVertice(v1)

        if ClassV2 == None:
            ClassV2 = self.vertices.buscaVertice(v2)

        if ClassV2 != None:
            ClassV1.addAresta(v1, v2, ClassV2, peso, info)

        return True

    def print(self, x=1):
        self.vertices.print(x)

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

        # informações uteis
        distancias = [0 for i in range(self.maxId - 1)]
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
                    distancias[u.getInfo()[1]] += 1
                    fila.enfileira( v )

        tam = len(distancias)
        tam -= 1
        while distancias[tam] == 0:
            distancias.pop(-1)
            tam -= 1

        print("BSF concluída")
        print(distancias)
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

        print("DFS iniciada")
        self.tempo = 0
        while len(Vertices) != 0:
            if u.getInfo()[0] == 'b':
                self.DFS_Visit(Vertices, u)
            if len(Vertices) != 0:
                u = Vertices[0]
                Vertices.pop(0)
        self.print(3)
        self.vertices.setInfoVerts(None,None)
        #self.print(3)
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
        # Dificil esse eim...
        print(self.DFS_Khan())

    def DFS_2_(self, first=None):
        if first != None and type(first) != type(""):
            return None


        if first != None:
            inicio = self.vertices.buscaVertice(first)
            if inicio == None:
                inicio = Vertices[0]
        else:
            inicio = Vertices[0]


        visitados = [False for i in range (self.maxId)]
        pilha = pl.pilha()


        while True:

            aux = None
            if not visitados[inicio.getId()]:
                visitados[inicio.getId()] = True
                pilha.empilha(inicio)

            achou = False

            arestas = inicio.getListClassVertArestas()
            for aresta in arestas:
                if not visitados[aresta.getId()]:
                    #print("Encontrei uma aresta ")
                    aux = aresta
                    achou = True
                    break

            if achou:
                inicio = aux
            else:
                pilha.desempilha()
                #print("Desempilhei a aresta")
                if pilha.vazia():
                    break
                inicio = pilha.getTopo()

        #self.print(3)    
    def FriendsForMe(self, inicio):
        me = self.vertices.buscaVertice(inicio)
        amigos = me.getListClassVertArestas()
        setAmigos = []

        for amigo in amigos:
            setAmigos.append(amigo.getListClassVertArestas())

        amigosEmComum = set()

        amigosEmComum = set(setAmigos[0])
        for i in range( 1, len(setAmigos)):
            amigosEmComum = amigosEmComum.intersection(set(setAmigos[i])) 


        return amigosEmComum


    def FloydWarshall(self):
        dist = self.vertices.getMatrizAdjPesos()
        pred = self.vertices.getMatrizAdj()
        n = self.maxId

        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] == 0:
                    dist[i][j] = math.inf
                elif dist[i][j] != 0:
                    pred[i][j] = i

        if n < 20:
            for i in dist:
                print(i)
            print()

        print("FloydWarshall iniciado")
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > (dist[i][k] + dist[k][j]):
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]
        print("FloydWarshall concluido")

        if n < 20:
            print()
            for i in dist:
                print(i)

            print()
            for i in pred:
                print(i)

    def getVertices(self):
        return self.vertices.getVerts()


if __name__ == '__main__':
    g = grafo('amigos.txt')

    '''
    Grafo denso desordenado   

    for i in range(100000):
        g.addAresta(str(random.randrange(100)), str(random.randrange(100)))
    print("Insercao concluida")
    '''

    # Se der azar é possivel acontecer aki tambem o q acontece no semi ordenado para DSP(recursivo)
    # FloydWarshal(FW) demora muito mesmo com +1000 elementos
    # FW com 500 demora, mas termina kk


    # Semi ordenado
    '''
    for i in range(1000):
        g.addAresta(str(i), str(i+1))
    print("Insercao concluida")
    '''
    # Para DFS recursiva, com ~1000 (- q isso funciona) elementos neste modo, alcança
    # a profundidade maxima da recursao e retorna um erro
    '''
    maluco = g.getVertices()[0].getRot()
    print(maluco)
    print(len(g.FriendsForMe(maluco)))
    for i in g.FriendsForMe(maluco):
        print(i.getRot())

    g.addAresta('1', '2', 3)
    g.addAresta('1', '5', -4)
    g.addAresta('1', '3', 8)
    g.addAresta('2', '4', 1)
    g.addAresta('2', '5', 7)
    g.addAresta('3', '2', 4)
    g.addAresta('4', '3', -5)
    g.addAresta('4', '1', 2)
    g.addAresta('5', '4', 6)
    '''

    #g.DFS_2_('1')
    #g.print()
    #g.BFS('10')
    #g.DFS()
    #g.Khan()
    #g.FloydWarshall()
