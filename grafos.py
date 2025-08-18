from abc import ABC, abstractmethod 


class Grafo(ABC):

    @abstractmethod
    def numero_de_vertices(self):
        pass

    @abstractmethod
    def numero_de_arestas(self):
        pass

    @abstractmethod
    def sequencia_de_graus(self):
        pass

    @abstractmethod
    def adicionar_aresta(self, u, v):
        pass

    @abstractmethod
    def remover_aresta(self, u, v):
        pass

    @abstractmethod
    def imprimir(self):
        pass

class GrafoDenso(Grafo):
    def __init__(self, vertices):
        if isinstance(vertices, int):
            self.rotulos = [str(i) for i in range(vertices)]
        else:
            self.rotulos = vertices
        
        n = len(self.rotulos)
        self.matriz = [[0 for _ in range(n)] for _ in range(n)]

    def numero_de_vertices(self):
        return len(self.rotulos)

    def numero_de_arestas(self):
        count = 0
        n = len(self.rotulos)
        for i in range(n):
            for j in range(i+1, n):  # só conta uma vez
                if self.matriz[i][j] == 1:
                    count += 1
        return count

    def sequencia_de_graus(self):
        graus = []
        n = len(self.rotulos)
        for i in range(n):
            grau = sum(self.matriz[i])
            graus.append(grau)
        return graus

    def adicionar_aresta(self, u, v):
        i, j = self.rotulos.index(u), self.rotulos.index(v)
        self.matriz[i][j] = 1
        self.matriz[j][i] = 1  # grafo não direcionado

    def remover_aresta(self, u, v):
        i, j = self.rotulos.index(u), self.rotulos.index(v)
        self.matriz[i][j] = 0
        self.matriz[j][i] = 0

    def imprimir(self):
        print("   ", " ".join(self.rotulos))
        for i, linha in enumerate(self.matriz):
            print(self.rotulos[i], linha)

if __name__ == "__main__":
    V = ["A","B","C","D","E"]
    grafo = GrafoDenso(V)

    # adicionando arestas
    arestas = [("A","B"), ("A","C"), ("C","D"), ("C","E"), ("B","D")]
    for u, v in arestas:
        grafo.adicionar_aresta(u, v)

    print("Grafo inicial:")
    grafo.imprimir()
    print("Número de vértices:", grafo.numero_de_vertices())
    print("Número de arestas:", grafo.numero_de_arestas())
    print("Sequência de graus:", grafo.sequencia_de_graus())

    # removendo (A,C)
    grafo.remover_aresta("A","C")
    print("\nGrafo após remover (A,C):")
    grafo.imprimir()

