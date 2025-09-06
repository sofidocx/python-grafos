import networkx as nx

def verificar_isomorfismo(grafo1, grafo2):
   
    if nx.is_isomorphic(grafo1, grafo2):
        print("Os grafos são isomorfos.")
        return True
    else:
        print("Os grafos NÃO são isomorfos.")
        return False


print("--- Exemplo 1: Grafos isomorfos ---")

G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])


G2 = nx.Graph()
G2.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

verificar_isomorfismo(G1, G2)
print("-" * 30)


print("--- Exemplo 2: Grafos não isomorfos ---")

G3 = nx.Graph()
G3.add_edges_from([(1, 2), (2, 3), (3, 4)])


G4 = nx.Graph()
G4.add_edges_from([(10, 20), (20, 30), (30, 40)])

verificar_isomorfismo(G1, G3)
verificar_isomorfismo(G3, G4)
print("-" * 30)


print("--- Exemplo 3: Outro par de grafos não isomorfos ---")

G5 = nx.Graph()
G5.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D')])


G6 = nx.Graph()
G6.add_edges_from([(1, 2), (2, 3), (3, 4)])

verificar_isomorfismo(G5, G6)
print("-" * 30)
