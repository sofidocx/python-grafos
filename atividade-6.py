from abc import ABC, abstractmethod

class Grafo(ABC):
    @abstractmethod
    def get_vertices(self):
        pass

    @abstractmethod
    def get_arestas(self):
        pass

    @abstractmethod
    def is_subgrafo(self, outro_grafo):
        pass

    @abstractmethod
    def is_subgrafo_gerador(self, outro_grafo):
        pass

    @abstractmethod
    def is_subgrafo_induzido(self, outro_grafo):
        pass


class GrafoDenso(Grafo):
    def __init__(self, vertices, arestas):
        """
        Inicializa o grafo denso com lista de vértices e arestas.
        :param vertices: Lista de vértices
        :param arestas: Lista de arestas (tuplas de vértices)
        """
        self.vertices = vertices
        self.arestas = arestas

    def get_vertices(self):
        return self.vertices

    def get_arestas(self):
        return self.arestas

    def is_subgrafo(self, outro_grafo):
        """
        Verifica se o grafo atual é subgrafo de outro grafo.
        :param outro_grafo: Grafo para comparar
        :return: True se for subgrafo, False caso contrário
        """
        
        if not all(v in outro_grafo.get_vertices() for v in self.get_vertices()):
            return False

        
        for aresta in self.get_arestas():
            if aresta not in outro_grafo.get_arestas():
                return False

        return True

    def is_subgrafo_gerador(self, outro_grafo):
        """
        Verifica se o grafo atual é um subgrafo gerador do outro grafo.
        :param outro_grafo: Grafo para comparar
        :return: True se for subgrafo gerador, False caso contrário
        """
        
        if not all(v in outro_grafo.get_vertices() for v in self.get_vertices()):
            return False

        
        for aresta in self.get_arestas():
            if aresta not in outro_grafo.get_arestas():
                return False

        return True

    def is_subgrafo_induzido(self, outro_grafo):
        """
        Verifica se o grafo atual é um subgrafo induzido do outro grafo.
        :param outro_grafo: Grafo para comparar
        :return: True se for subgrafo induzido, False caso contrário
        """
        
        if not all(v in outro_grafo.get_vertices() for v in self.get_vertices()):
            return False

     
        for aresta in self.get_arestas():
            v1, v2 = aresta
            if v1 not in self.get_vertices() or v2 not in self.get_vertices():
                return False
            if aresta not in outro_grafo.get_arestas():
                return False

        return True


class GrafoEsparto(Grafo):
    def __init__(self, vertices, arestas):
        """
        Inicializa o grafo esparso com lista de vértices e arestas.
        :param vertices: Lista de vértices
        :param arestas: Lista de arestas (tuplas de vértices)
        """
        self.vertices = vertices
        self.arestas = arestas

    def get_vertices(self):
        return self.vertices

    def get_arestas(self):
        return self.arestas

    def is_subgrafo(self, outro_grafo):
        """
        Verifica se o grafo atual é subgrafo de outro grafo.
        :param outro_grafo: Grafo para comparar
        :return: True se for subgrafo, False caso contrário
        """
        
        if not all(v in outro_grafo.get_vertices() for v in self.get_vertices()):
            return False

        
        for aresta in self.get_arestas():
            if aresta not in outro_grafo.get_arestas():
                return False

        return True

    def is_subgrafo_gerador(self, outro_grafo):
        """
        Verifica se o grafo atual é um subgrafo gerador do outro grafo.
        :param outro_grafo: Grafo para comparar
        :return: True se for subgrafo gerador, False caso contrário
        """
        
        if not all(v in outro_grafo.get_vertices() for v in self.get_vertices()):
            return False

        
        for aresta in self.get_arestas():
            if aresta not in outro_grafo.get_arestas():
                return False

        return True

    def is_subgrafo_induzido(self, outro_grafo):
        """
        Verifica se o grafo atual é um subgrafo induzido do outro grafo.
        :param outro_grafo: Grafo para comparar
        :return: True se for subgrafo induzido, False caso contrário
        """
      
        if not all(v in outro_grafo.get_vertices() for v in self.get_vertices()):
            return False

       
        for aresta in self.get_arestas():
            v1, v2 = aresta  # Supondo que as arestas sejam representadas como tuplas de vértices
            if v1 not in self.get_vertices() or v2 not in self.get_vertices():
                return False
            if aresta not in outro_grafo.get_arestas():
                return False

        return True




# Criando grafos densos e esparsos
vertices_grafo_denso = [1, 2, 3, 4]
arestas_grafo_denso = [(1, 2), (2, 3), (3, 4), (4, 1)]
grafo_denso = GrafoDenso(vertices_grafo_denso, arestas_grafo_denso)

vertices_grafo_esparso = [1, 2, 3]
arestas_grafo_esparso = [(1, 2), (2, 3)]
grafo_esparso = GrafoEsparto(vertices_grafo_esparso, arestas_grafo_esparso)

# Verificando se o grafo esparso é subgrafo de grafo denso
print(grafo_esparso.is_subgrafo(grafo_denso))  # Retorna True ou False

# Verificando se o grafo esparso é subgrafo gerador do grafo denso
print(grafo_esparso.is_subgrafo_gerador(grafo_denso))  # Retorna True ou False

# Verificando se o grafo esparso é subgrafo induzido do grafo denso
print(grafo_esparso.is_subgrafo_induzido(grafo_denso))  # Retorna True ou False
