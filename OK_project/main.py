import graphviz
import random
from collections import defaultdict

def best_path(tab):
    tmp = []
    for i in range(len(tab)):
        tmp.append(len(tab[i]))
    if len(tmp) == 0: return "Brak przejścia"
    minimum = min(tmp)
    results = []
    for i in range(len(tab)):
        if tmp[i] == minimum: results.append(tab[i])
    return results


class Graphs:
    def __init__(self, verticles):
        self.V = verticles
        self.graph = defaultdict(list)
        self.paths = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def recursiveDFS(self, u, d, visited, path):  # DFS
        visited[u] = True
        path.append(u)
        if u == d:
            tmp = path[:]
            self.paths.append(tmp)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.recursiveDFS(i, d, visited, path)
        path.pop()
        visited[u] = False

    def allPaths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.recursiveDFS(s, d, visited, path)


def in_tab(tab, vari):
    for i in tab:
        if i == vari: return 1
    return 0

def toGraphViz(n, graphs, q, g):
    gViz = graphviz.Graph("Graph " + str(q))
    for i in range(n):
        gViz.node(str(i) + '_' + str(q), str(i) + '_' + str(q))
        for j in range(i + 1, len(graphs[i])):
            if graphs[i][j] == 1:
                g.addEdge(i, j)
                gViz.edge(str(i) + '_' + str(q), str(j) + '_' + str(q))
    return gViz


ni_all = graphviz.Graph('Graf i jego rodzina')

n = 6  # liczba wierzcholkow grafu
a = []
ni = graphviz.Graph('Graf podstawowy')
for i in range(n):
    tmp = []
    for j in range(n):
        if j > i:
            rand = int(random.randrange(0, 2))  # do poprawy?
            tmp.append(rand)
        else:
            tmp.append(0)
    a.append(tmp)
g = Graphs(n)
for i in range(n):
    ni.node(str(i), str(i))
    for j in range(i + 1, len(a[i])):
        if a[i][j] == 1:
            g.addEdge(i, j)
            ni.edge(str(i), str(j))
g.allPaths(0, n - 1)
print("Best path for main graph: ", best_path(g.paths))

ni_all.subgraph(ni)
subg = []  # list od subgrafów
numb_g = 3 #liczba generowanych grafow
for i in range(numb_g):
    tmpg = []
    for k in range(n):
        tmp = []
        for j in range(n):
            if a[k][j] == 1:
                rand = int(random.randrange(0, 2))
            else:
                rand = 0
            tmp.append(rand)
        tmpg.append(tmp)
    subg.append(tmpg)
for i in range(numb_g):
    g = Graphs(n)
    nitmp = toGraphViz(n, subg[i], i + 1, g)
    g.allPaths(0, n - 1)
    print("Best path for subgraph", i + 1, best_path(g.paths))
    ni_all.subgraph(nitmp)


#print(ni_all.source)
ni_all.view()