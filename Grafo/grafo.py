import vertice as vt
import vertices as vts
import aresta as ar
import arestas as ars
import fila as fl
import pilha as pl
import estatistic as est
import math
import numpy as np
from operator import attrgetter


class grafo(object):
    def __init__(self):
        self.vertices = vts.vertices()
        self.maxId = 0  # indicador de quantidade e controle para uso do FloydWarshall
        self.tempo = 0

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

    def getQtdeVertices(self):
        return self.maxId

    def getQtdeArestas(self):
        return self.vertices.getQtdeArestas()

    def getQntdeVertice(self):
        return self.maxId

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
            ClassV2.addAresta(v2, v1, ClassV1, peso, info) # Nao orientado

        return True

    def print(self, x=1):
        self.vertices.print(x)

    def BFS(self, inicio):
        if type(inicio) != type(""):
            return None
        self.vertices.setInfoVerts(v1=None, info=['b', math.inf, None])

        #######################################################
        #print("Inicial: ")
        #print(inicio)
        #######################################################

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

        #print("BFS iniciada")
        while not fila.vazia():
            u = fila.desenfileira()
            for v in u.getListClassVertArestas():
                #print(v)
                infoV = v.getInfo()
                if infoV[0] == 'b':
                    v.setInfo(['c', u.getInfo()[1]+1, u.getRot()])
                    distancias[u.getInfo()[1]] += 1
                    fila.enfileira( v )
            infoU = u.getInfo()
            u.setInfo(['p', infoU[1], infoU[2]])
        #print("BSF concluída")

        while 0 in distancias:
            distancias.remove(0)

        #######################################################
        '''
        print()
        maisDistantes = []
        md = self.vertices.getVerts()
        for v in md:
            infoV = v.getInfo()
            if infoV[1] == len(distancias)-1:
                maisDistantes.append(v)
        
        for i in maisDistantes[:10]:
            print(i.getRot())
        
        exit(0)
        '''
        #######################################################

        #print(distancias)
        if self.maxId < 20:
            self.print(3)
        
        self.vertices.setInfoVerts(v1=None, info=None)
        return distancias

    def analises_BFS(self):
        vertices = [i.getRot() for i in self.vertices.getVerts()] # Pego o nome de todos os vertices
        distancias = [self.BFS(i) for i in vertices] # Executo para todos os vertices uma BFS
        #var_all = est.varN(distancias) # Calculo a variancia de todos
        #dp_all = est.dpN(distancias) # Desvio padrao de todos
        #min_max = est.minmaxN(distancias) # MinMax aplicado ao normalizador - Normalização
        sum_total = est.sumN(distancias) # Soma cada coluna de distancia
        
        amount = len(distancias)
        avg_total = [ i/amount for i in sum_total]

        print("\nSoma total de cada nível de distancias")
        distancia = 1
        for i in sum_total:
            print("{} - {}".format(distancia,i))
            distancia += 1
        
        print("\nMedia de cada distancia")
        distancia = 1
        for i in avg_total:
            print("{} - {}".format(distancia,i))
            distancia += 1

    ##############################################################################################
    ##################################### Funcoes sem testes #####################################
    def Dijkstra(self, inicio):
        self.vertices.setInfoVerts(v1=None  , info=math.inf)
        self.vertices.setInfoVerts(v1=inicio, info=0)
        Q = self.vertices.getVerts()
        p = [None for v in range(self.vertices.getQtde())]
        
        while len(Q) != 0:
            u = min(Q,key=attrgetter('info'))
            Q.remove(u)
            for a in u.getListClassArestas():
                if u.getInfo() > a.getClassDest().getInfo() + a.getPeso():
                    u.setInfo( a.getClassDest().getInfo() + a.getPeso() ) # relaxamento
                    p[u.getId()] = a.getClassDest()

    def BellmanFord(self, inicio):
        qtde = self.vertices.getQtde()
        d = [0 for v in range(qtde)]
        p = [None for v in range(qtde)]

        v0 = self.vertices.buscaVertice(inicio)

        d[v0.getId()] = 0
        relaxou = True
        for i in range(qtde):
            relaxou = False
            for v in self.vertices.getVerts():
                for a in v.getListClassArestas():
                    if d[v.getId()] > d[a.getClassDest().getId()] + a.getPeso():
                        d[v.getId()] = d[a.getClassDest().getId()] + a.getPeso() # relaxamento
                        p[v.getId()] = a.getClassDest()
                        relaxou = True
            if not relaxou:
                break
    
    def FordFulkerson(self, fontes, sorvedouros):
        self.vertices.setInfoArestas(0)
        
        pass
    ##############################################################################################
    def DFSRec(self, inicio=None):
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

        print("DFS concluida")
        #self.print(3)
        self.vertices.setInfoVerts(None,None)

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

    def DFS(self, first=None, tipo=None):
        if first != None and type(first) != type(""):
            return None
        self.vertices.setInfoVerts(v1=None, info=['b', None, math.inf, math.inf])

        Vertices = self.vertices.getVerts()
        if first != None:
            inicio = self.vertices.buscaVertice(first)
            if inicio == None:
                inicio = Vertices[0]
        else:
            inicio = Vertices[0]

        visitados = [False for i in range (self.maxId)]
        pilha = pl.pilha()

        ciclo = False
        tempo = 0
        while True:
            aux = None
            if not visitados[inicio.getId()]:
                tempo += 1
                info = inicio.getInfo()
                inicio.setInfo(['c', info[1], tempo, info[3]])
                visitados[inicio.getId()] = True
                pilha.empilha(inicio)

            achou = False

            arestas = inicio.getListClassVertArestas()
            for aresta in arestas:
                if not visitados[aresta.getId()]:
                    aux = aresta
                    info = aux.getInfo()
                    aux.setInfo([ info[0], inicio.getRot() ,info[2] ,info[3] ])
                    achou = True
                    break
                elif not ciclo:
                    if aresta.getInfo()[0] == 'c' or aresta.getInfo()[0] == 'p':
                        ciclo = True
                        if tipo == 1:
                            return True

            if achou:
                inicio = aux
            else:
                u = pilha.desempilha()
                tempo += 1
                info = u.getInfo()
                u.setInfo(['p', info[1],info[2], tempo])
                if pilha.vazia():
                    break
                inicio = pilha.getTopo()
        if self.maxId < 20:
            self.print(3)


        results = []
        results.append(ciclo)
        return results

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

    def Khan(self):
        #r = self.DFS()
        #print(r[0])
        visitados = [False for i in range (self.maxId)]
        arestas = self.vertices.getArestasSort()
        fontes = self.vertices.getFontes()
        listaOrdenada = []
        while len(fontes) != 0:
            n = fontes.pop(0)
            listaOrdenada.append(n)
            
            pass
'''
if __name__ == '__main__':
    g = grafo()
    #g.load_nodes('amigos.txt')
    g.addAresta('142', '143')
    g.addAresta('143', '321')
    g.addAresta('143', '341')
    g.addAresta('143', '370')
    g.addAresta('143', '378')
    g.addAresta('321', '322')
    g.addAresta('321', '326')
    g.addAresta('341', '401')
    g.addAresta('378', '401')
    g.addAresta('326', '421')
    g.addAresta('326', '401')
    g.addAresta('322', '421')
    g.addAresta('322', '401')
    print("Insercao concluida")
    print("Quantidade de vertices inseridos: {}".format(g.getQtdeVertices()))
    print("Quantidade de arestas existentes: {}".format(g.getQtdeArestas()))
    
    g.Khan()
'''
    #g.FloydWarshall()
    #g.BFS('1')
'''
    #me = g.getVertices()[0].getRot()
    me = '3'
    print("\nVertice analisado: {}".format(me))
    friends = g.FriendsForMe(me)
    print("Total de amigos encontrados: {}".format(len(friends)))
    p = [i.getRot() for i in friends]

    print(p)

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

#def testes():
    #g = grafo()

    # Grafo denso
    # Desordenado
'''
    for i in range(1000000):
        g.addAresta(str(random.randrange(500)),str(random.randrange(400)))
'''
    # Se der azar é possivel acontecer aki tambem o q acontece no semi ordenado para DSP(recursivo)
    # FloydWarshal(FW) demora muito mesmo com +1000 elementos
    # FW com 500 demora, mas termina kk

    # Semi ordenado
'''
    for i in range(1000):
        g.addAresta(str(i), str(i+1))
'''
    # Para DFS recursiva, com ~1000 (- q isso funciona) elementos neste modo, alcança
    # a profundidade maxima da recursao e retorna um erro

    # Grafo simples
'''
    g.addAresta('1', '2', 3)
    g.addAresta('1', '6', -4)
    g.addAresta('2', '3', 8)
    g.addAresta('2', '5', 1)
    g.addAresta('3', '6', 7)
    g.addAresta('6', '1', 4)
'''

    #me = g.getVertices()[0].getRot()
'''
    print("\nVertice analisado: {}".format(me))
    friends = g.FriendsForMe(me)
    print("Total de amigos encontrados: {}".format(len(friends)))
    p = []
    for i in friends:
        p.append(i.getRot())
    print(p)
'''
