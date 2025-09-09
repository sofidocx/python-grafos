class GrafoEsparso:
    def __init__(self, labels):
        self.labels = labels
        self.num_vertices = len(labels)
        self.adjacencias = {label: [] for label in labels}
        self.vertices = labels

    def adicionar_aresta(self, v_origem, v_destino):
        self.adjacencias[v_origem].append(v_destino)
        self.adjacencias[v_destino].append(v_origem)
    
    def get_arestas(self):
        arestas = []
        for v_origem, vizinhos in self.adjacencias.items():
            for v_destino in vizinhos:
                if (v_destino, v_origem) not in arestas:
                    arestas.append((v_origem, v_destino))
        return arestas

    def _eh_seguro(self, vertice, cor, cores_atribuidas):
        """Verifica se a atribuição de uma cor a um vértice é segura."""
        for vizinho in self.adjacencias[vertice]:
            if vizinho in cores_atribuidas and cores_atribuidas[vizinho] == cor:
                return False
        return True

    def _colorir_backtracking(self, vertice_idx, m, cores_atribuidas, cores_usadas):
        """Função recursiva para o algoritmo de backtracking."""
        if vertice_idx == self.num_vertices:
            return True, m

        vertice_atual = self.vertices[vertice_idx]

        for cor in range(1, m + 1):
            if self._eh_seguro(vertice_atual, cor, cores_atribuidas):
                cores_atribuidas[vertice_atual] = cor

                solucao_encontrada, _ = self._colorir_backtracking(vertice_idx + 1, m, cores_atribuidas, cores_usadas)
                if solucao_encontrada:
                    return True, m
                
                
                cores_atribuidas.pop(vertice_atual)

        return False, m

    def colorir_grafo(self):
        """Encontra a coloração do grafo usando o número mínimo de cores."""
        num_minimo_cores = 1
        
        while True:
            cores_atribuidas = {}
            sucesso, _ = self._colorir_backtracking(0, num_minimo_cores, cores_atribuidas, set())
            
            if sucesso and len(cores_atribuidas) == self.num_vertices:
                
                return num_minimo_cores, cores_atribuidas
            
            num_minimo_cores += 1
            if num_minimo_cores > self.num_vertices: # Limite de segurança
                return -1, {}


if __name__ == "__main__":
    aulas = ['M', 'A', 'C', 'F', 'Q', 'P']
    g = GrafoEsparso(labels=aulas)


    g.adicionar_aresta('C', 'F')
    g.adicionar_aresta('C', 'A')
    g.adicionar_aresta('F', 'A')
    g.adicionar_aresta('M', 'P')
    g.adicionar_aresta('M', 'A')
    g.adicionar_aresta('P', 'A')
    g.adicionar_aresta('Q', 'F')

    
    print("Conflitos de aulas:")
    for v_origem, v_destino in g.get_arestas():
        print(f"- Aula {v_origem} tem conflito com: {v_destino}")
    print("-" * 30)

    
    numero_minimo_horarios, cores_atribuidas = g.colorir_grafo()

    if numero_minimo_horarios != -1:
        print(f"Número mínimo de horários necessários (Número Cromático Chi(G)): {numero_minimo_horarios}")
        print("Atribuição de cores:")
        print(cores_atribuidas)
    else:
        print("Não foi possível encontrar uma solução de coloração.")