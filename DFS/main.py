from collections import defaultdict

class Graph():
	def __init__(self,vertices):
		self.graph = defaultdict(list)
		self.V = vertices

def edgeAdder(graph,u,v):
	graph.graph[u].append(v)

def cycle(graph, v, visited, recStack):
	visited[v] = True
	recStack[v] = True
	for neighbour in graph.graph[v]:
		if visited[neighbour] == False:
			if cycle(graph,neighbour, visited, recStack) == True:
				return True
		elif recStack[neighbour] == True:
			return True
	recStack[v] = False
	return False

def isCyclic(graph):
	visited = [False] * (graph.V + 1)
	recStack = [False] * (graph.V + 1)
	for node in range(graph.V):
		if visited[node] == False:
			if cycle(graph,node,visited,recStack) == True:
				return True
	return False

#visited = set()

'''def DFSms(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	print(start)
	for i in graph.graph[start]:
		DFSms(graph,i,visited)'''
tab_DFS = []
def DFSms(graph,v,visited):
	visited.add(v)
	tab_DFS.append(v)
	print(v, end=' ')
	for i in graph.graph[v]:
		if i not in visited:
			DFSms(graph,i,visited)

def DFS_msasiedztwa(graph,v):
	visited = set()
	DFSms(graph,v,visited)


def DEL_msasiedztwa(graph):
	in_d = [0] * (graph.V)
	for i in graph.graph:
		for j in graph.graph[i]:
			in_d[j] += 1
	q = []
	for i in range(graph.V):
		if in_d[i] == 0:
			q.append(i)
	cnt = 0
	top = []
	while q:
		u = q.pop(0)
		top.append(u)
		for i in graph.graph[u]:
			in_d[i] -= 1
			if in_d[i] == 0:
				q.append(i)
	print(top)

tab = []
n = int(input("Liczba wierzcholkow: "))
e= int(input("Liczba krawedzi: "))
for i in range(e):
	q = list(map(int,input().split(" ")))
	tab.append(q)
g=Graph(n)
#print(tab)
for i in range(e):
	edgeAdder(g,tab[i][0],tab[i][1])
if isCyclic(g)==1:
	print("Graf zawiera cykl. Sortowanie niemożliwe.")
else:
	DFS_msasiedztwa(g,5)
	print(tab_DFS)
	DEL_msasiedztwa(g)

'''print("Klawiatura (K) czy plik (P)?")
odp=input()
tab = []
if odp=="K":
    n = int(input())
    e= int(input())
    for i in range(e):
        q = input().split(" ")
        tab.append(q)
    #
    print(tab)
    for i in tab:
        edge(graph,tab[0],tab[1])
    print(edges_generator(graph))
    #
elif odp=="P":
    x=input("Podaj nazwe lub sciezke pliku: ")
    try:
        f = open(x, "r")
        for i in f:
            print(i)
    except:
        print("Taki plik nie istnieje lub ma bledne dane!")
else:
    print("Bledna odpowiedz!")'''