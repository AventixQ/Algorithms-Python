from collections import defaultdict
from random import random
from itertools import combinations
from networkx.generators.random_graphs import erdos_renyi_graph
import time
import math


# from networkx.generators.random_graphs import erdos_renyi_graph


class Error(Exception):
    """Base class for other exceptions"""
    pass


class BadValue(Error):
    """Bad input value"""
    pass


class DoubledValue(Error):
    """Doubled value"""
    pass


class AdjGraph():
    def __init__(self, size):
        self.adjMatrix = []
        for x in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.V = size
        self.edges = 0
        self.path = []
        self.vd = [0] * size

    def add_edges(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        self.edges += 1
        self.vd[v1] += 1
        self.vd[v2] += 1

    def print(self):
        for x in self.adjMatrix:
            for val in x:
                print(val, end=" ")
            print()

    def printpath(self, path, q):
        for vrt in path:
            print(vrt + q, end=" ")
        print(path[0], "\n")

    # Hamilton
    def check(self, path, vertex, pos):
        if self.adjMatrix[path[pos - 1]][vertex] == 0:
            return False

        for x in path:
            if vertex == x:
                return False
        return True

    def hamiltonrec(self, path, pos):
        if pos == self.V:
            if self.adjMatrix[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):
            if self.check(path, v, pos):
                path[pos] = v
                if self.hamiltonrec(path, pos + 1):
                    return True
            path[pos] = -1
        return False

    def hamiltonian(self, q):
        path = [-1] * self.V
        path[0] = 0
        if not self.hamiltonrec(path, 1):
            print("Graf wejściowy nie zawiera cyklu.\n")
            return False

        self.printpath(path, q)
        return True

    # Euler
    def isEuler(self):
        for x in range(self.V):
            s = 0
            for y in range(self.V):
                s += self.adjMatrix[x][y]
            if s % 2 == 1:
                return False
        return True

    def dfs_euler(self, v):
        for i in range(self.V):
            while self.adjMatrix[v][i]:
                self.adjMatrix[v][i] = 0
                self.adjMatrix[i][v] = 0
                self.dfs_euler(i)
        self.path.append(v)

    def dfsb(self, v, vf, D, cv):
        D[v] = cv
        low = cv
        cv += 1
        for u in range(self.V):
            if u != vf and self.adjMatrix[v][u]:
                if D[u] == 0:
                    temp = self.dfsb(u, v, D, cv)
                    if temp < low:
                        low = temp
                elif D[u] < low:
                    low = D[u]
        if vf > -1 and low == D[v]:
            self.adjMatrix[vf][v] = self.adjMatrix[v][vf] = 2
        return low

    def findEuler(self, v):
        S = []
        while True:
            S.append(v)
            u = 0
            while u < self.V and not self.adjMatrix[v][u]:
                u += 1
            if u == self.V:
                break
            D = [0] * self.V
            cv = 1
            self.dfsb(v, -1, D, cv)

            w = u + 1
            while self.adjMatrix[v][u] == 2 and w < self.V:
                if self.adjMatrix[v][w]:
                    u = w
                w += 1
            self.adjMatrix[v][u] = self.adjMatrix[u][v] = 0
            v = u
        return S


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices


def edgeAdder(graph, u, v):
    graph.graph[u].append(v)


def find_min(tab, e):
    mini = 99999999
    for i in range(e):
        if tab[i][0] < mini: mini = tab[i][0]
        if tab[i][1] < mini: mini = tab[i][1]
    return mini


global visited
visited = 0
P = []


def hamiltonianL(graph, ver, O, n, P):
    O[ver] = 1
    P.append(ver)
    global visited
    visited += 1
    # print(P,visited)
    # print(graph.V)
    # print(graph.graph[ver])
    for i in graph.graph[ver]:
        # print(i)
        # P.append(ver)
        if i == start and visited == n:
            P.append(start)
            return True
        if not O[i]:
            if hamiltonianL(graph, i, O, n, P):
                # P.append(ver)
                return True
    O[ver] = 0
    visited -= 1
    del P[-1]
    return False


def Hcycle(graph, O, n):
    # for i in range(n):
    # O[i] = False
    # P.append(0)
    global start
    start = 0
    global visited
    visited = 0
    # k=1
    global P
    hamiltonianL(graph, start, O, n, P)


def eulerianL(graph):
    a = graph
    e_count = dict()
    for i in range(a.V):  # wcześniej było range(len(a.graph))
        e_count[i] = len(a.graph[i])
    path = [0]
    c = []
    # path.append(0)
    ver = 0
    if len(a.graph) == 0: return False
    while len(path):
        if e_count[ver]:
            path.append(ver)
            next_ver = a.graph[ver][-1]
            e_count[ver] -= 1
            a.graph[ver].pop()
            ver = next_ver
        else:
            c.append(ver)
            ver = path[-1]
            path.pop()
    c.reverse()
    if c[0] == c[-1]:
        return c
    else:
        return False


def ER(n, p):
    V = set([v for v in range(n)])
    E = []
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.append(combination)
    return E


density = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
cases = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28,30]

while True:
    print("1 - Dane wczytane z klawiatury\n2 - Dane wczytane z pliku\n3 - Zakończ")
    choice = input()
    vertexes = []
    if choice == "1":
        while True:
            try:
                print("Podaj ilosc wierzchołków krawędzi : ")
                v, e = map(int, input().split(" "))
                break
            except ValueError:
                print("Podaj poprawne dane!")
        print("Podaj krawędzie")
        y = 0
        while y < e:
            try:
                x = input().strip()
                i = x.split()
                p = [int(j) for j in i]
                if len(p) != 2:
                    raise BadValue
                else:
                    if p not in vertexes:
                        vertexes.append(p)
                        y += 1
                    else:
                        raise DoubledValue
            except ValueError:
                print("To nie jest poprawna wartość!")
            except BadValue:
                print("Podano złe wartości krawędzi")
            except DoubledValue:
                print("Taka wartość już istnieje nie można jej dodać ponownie!")

        gL = Graph(v)  # Lista następników od 0
        q = find_min(vertexes, e)
        # print(vertexes)

        if q != 0:
            for i in range(e):
                vertexes[i][0] = vertexes[i][0] - q
                vertexes[i][1] = vertexes[i][1] - q

        for i in range(e):
            edgeAdder(gL, vertexes[i][0], vertexes[i][1])

        O = []
        # P = []
        for i in range(v):
            O.append(0)

        print("\nCykl Hamiltona w grafie skierowanym: ")
        Hcycle(gL, O, v)
        if len(P) < v + 1:
            print("Graf wejściowy nie zawiera cyklu.")
        else:
            print([i + q for i in P])

        print("\nCykl Eulera w grafie skierowanym: ")
        result = eulerianL(gL)
        # result.reverse()
        if not result:
            print("Graf wejściowy nie zawiera cyklu.")
        else:
            print([i + q for i in result])
        print("\n")

        g = AdjGraph(v)  # Macierz sąsiedztwa od 0
        for edges in vertexes:
            v1, v2 = edges
            g.add_edges(v1, v2)

        print("\nCykl Hamiltona w grafie nieskierowanym: ")
        g.hamiltonian(q)

        print("Cykl Eulera w grafie nieskierowanym:")
        flag = True
        for v1 in range(g.V):
            if g.vd[v1]:
                break

        for i in range(v1, g.V):
            if g.vd[i] % 2 == 1:
                flag = False

        for i in range(v1, g.V):
            if g.vd[i] % 2:
                v1 = i
                break

        if flag:
            output = g.findEuler(v1)
            for x in output:
                print(x + q, end=" ")
            print("\n")
        else:
            print("Graf wejściowy nie zawiera cyklu.\n")
        # if g.isEuler():
        #     g.dfs_euler(0)
        #     for x in g.path:
        #         print(x, end=" ")
        #     print("\n")
        # else:
        #     print("Graf wejściowy nie zawiera cyklu.\n")
        del g
        del gL
        P = []
    if choice == "2":
        vertexes_file = []
        try:
            with open("cases.txt", 'r') as f:
                nol = 1
                for line in f:
                    if nol == 1:
                        vf, ef = map(int, line.split(" "))
                    else:
                        x = list(map(int, line.split()))
                        if x not in vertexes_file:
                            vertexes_file.append(x)
                        else:
                            raise DoubledValue
                    nol += 1
        except FileNotFoundError:
            print("Błędne dane lub taki plik nie istnieje!")
            continue
        except ValueError:
            print("Plik zawiera niepoprawne dane! Należy go sprawdzić!")
            continue
        except DoubledValue:
            print("Jedna z wartości wystepuje wielokrotnie i nie zostanie dodana! Sprawdź plik.")
            continue

        gL1 = Graph(vf)  # Lista następników od 0
        q = find_min(vertexes_file, ef)

        if q != 0:
            for i in range(e):
                vertexes_file[i][0] = vertexes_file[i][0] - q
                vertexes_file[i][1] = vertexes_file[i][1] - q

        for i in range(ef):
            edgeAdder(gL1, vertexes_file[i][0], vertexes_file[i][1])

        O = []
        # P = []
        for i in range(vf):
            O.append(0)

        print("\nCykl Hamiltona w grafie skierowanym: ")
        Hcycle(gL1, O, vf)
        if len(P) < vf + 1:
            print("Graf wejściowy nie zawiera cyklu.")
        else:
            print([i + q for i in P])

        print("\nCykl Eulera w grafie skierowanym: ")
        result = eulerianL(gL1)
        # result.reverse()
        if not result:
            print("Graf wejściowy nie zawiera cyklu.")
        else:
            print([i + q for i in result])
        print("\n")

        g1 = AdjGraph(vf)  # Macierz sąsiedztwa od 0
        for edges in vertexes_file:
            v1, v2 = edges
            g1.add_edges(v1, v2)

        print("\nCykl Hamiltona w grafie nieskierowanym: ")
        g1.hamiltonian(q)

        print("Cykl Eulera w grafie nieskierowanym:")
        flag = True
        for v1 in range(g1.V):
            if g1.vd[v1]:
                break

        for i in range(v1, g1.V):
            if g1.vd[i] % 2 == 1:
                flag = False

        for i in range(v1, g1.V):
            if g1.vd[i] % 2:
                v1 = i
                break

        if flag:
            output = g1.findEuler(v1)
            for x in output:
                print(x + q, end=" ")
            print("\n")
        else:
            print("Graf wejściowy nie zawiera cyklu.\n")

        del g1
        del gL1
        P = []
    if choice == "3":
        etap = 1
        for v in cases:
            czesc = 1
            # Tworznenie wierzchołków
            vertexes = []
            p = 0.5
            g = erdos_renyi_graph(v, p)
            vertexes = []
            for x in g.edges:
                vertexes.append(list(x))

            e = len(vertexes)

            # Macierz sąsiedzwtwa
            g = Graph(v)
            q = find_min(vertexes, e)

            if q != 0:
                for i in range(e):
                    vertexes[i][0] = vertexes[i][0] - q
                    vertexes[i][1] = vertexes[i][1] - q

            for i in range(e):
                edgeAdder(g, vertexes[i][0], vertexes[i][1])

            #print("{} z 10 / {} z 4".format(etap, czesc))
            tab_hl=[]
            avg_hl=0
            for x in range(1, 11):
                O = []
                for i in range(v):
                    O.append(0)
                print(x, end=" ")
                time_hl = time.time()
                Hcycle(g,O,v)
                end_hl = time.time() - time_hl
                tab_hl.append(end_hl)
                avg_hl += end_hl
            #tab_hl = []
            avg_hl = avg_hl / 10
            os_hl = 0
            for i in tab_hl:
                os_hl += (i - avg_hl) * (i - avg_hl)
            os_hl = math.sqrt(os_hl / 10)
            with open('HamiltonL.txt', 'a') as f:
                form = "{}\t{}\t{}\n".format(v, avg_hl, os_hl)
                f.write(form)
            czesc += 1
            #print("{} z 10 / {} z 4".format(etap, czesc))
            avg_el = 0
            tab_el = []
            for x in range(1, 11):
                print(x, end=" ")
                time_el = time.time()
                eulerianL(g)
                end_el = time.time() - time_el
                tab_el.append(end_el)
                avg_el += end_el
                #tab_el = []
            avg_el = avg_el / 10
            os_el = 0
            for i in tab_el:
                os_el += (i - avg_el) * (i - avg_el)
            os_DEL = math.sqrt(os_el / 10)
            with open('EulerL.txt', 'a') as f:
                form = "{}\t{}\t{}\n".format(v, avg_el, os_el)
                f.write(form)
            print("\n")

            czesc += 1
            #print("{} z 10 / {} z 4".format(etap, czesc))
            g1 = AdjGraph(v)
            for edges in vertexes:
                v1, v2 = edges
                g1.add_edges(v1, v2)
            avg_hm = 0
            t_hm = []
            for x in range(1, 11):
                print(x, end=" ")
                time_hm = time.time()
                g1.hamiltonian(0)
                end_hm = time.time() - time_hm
                t_hm.append(end_hm)
                avg_hm += end_hm
            avg_hm = avg_hm / 10
            os_hm = 0
            for i in t_hm:
                os_hm += (i - avg_hm) * (i - avg_hm)
            os_hm = math.sqrt(os_hm / 10)
            with open('HamiltonM.txt', 'a') as f:
                form = "{}\t{}\t{}\n".format(v, avg_hm, os_hm)
                f.write(form)
            print("\n")

            czesc += 1
            #print("{} z 10 / {} z 4".format(etap, czesc))
            avg_em = 0
            t_em = []
            for x in range(1, 11):
                print(x, end=" ")
                flag = True
                for v1 in range(g1.V):
                    if g1.vd[v1]:
                        break

                for i in range(v1, g1.V):
                    if g1.vd[i] % 2 == 1:
                        flag = False

                for i in range(v1, g1.V):
                    if g1.vd[i] % 2:
                        v1 = i
                        break
                time_em = time.time()
                if flag:
                    output = g1.findEuler(v1)
                #g1.findEuler(v)
                end_em = time.time() - time_em
                t_em.append(end_em)
                avg_em += end_em
            avg_em = avg_em / 10
            os_em = 0
            for i in t_em:
                os_em += (i - avg_em) * (i - avg_em)
            os_em = math.sqrt(os_em / 10)
            with open('EulerM.txt', 'a') as f:
                form = "{}\t{}\t{}\n".format(v, avg_em, os_em)
                f.write(form)
            print("\n")
            etap += 1
    if choice not in ["1", "2", "3"]:
        print("Podaj poprawną wartość!")
