import Grafos
import matplotlib.pyplot as plt
import networkx as nx
import hierarchyTree
filename = "data.txt"
f=open(filename,'r')
conteudo=f.read().split("\n")
vertices = conteudo[0].split(" ")
arestas = []
pesos = []
for j in range(1,len(conteudo)):
    valores = [conteudo[j].split(" ")[0],conteudo[j].split(" ")[1]]
    arestas.append(valores)
    pesos.append(int(conteudo[j].split(" ")[2]))
G = Grafos.Grafo(vertices, arestas,pesos)
G.Dijsktra("a")
for vertice in G.V:
    print(f"Vertice: {vertice.dado}")
    if vertice.caminhoPonderado!=None:
        for i in range(0,len(vertice.caminhoPonderado)):
            if i==len(vertice.caminhoPonderado)-1:
                print(f"{vertice.caminhoPonderado[i].dado}")
            else:
                print(f"{vertice.caminhoPonderado[i].dado}->", end="")
        print(f"Custo = {vertice.custoCaminho}")
    print("-------------------------------------")