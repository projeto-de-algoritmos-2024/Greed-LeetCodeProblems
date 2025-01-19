import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(
        self, qualidade: List[int], salario: List[int], k: int
    ) -> float:
        # Criamos uma lista de razões (salário / qualidade) para cada trabalhador
        # e ordenamos pela razão em ordem crescente.
        razao = sorted([(s / q, q) for s, q in zip(salario, qualidade)])
        
        # Usamos uma heap máxima (simulada com valores negativos) para rastrear as maiores qualidades.
        heap_maxima = []
        soma_qualidade = 0
        max_razao = 0.0
        
        # Inicializamos o heap e calculamos os valores para os primeiros k trabalhadores.
        for i in range(k):
            max_razao = max(max_razao, razao[i][0])  # Atualiza a maior razão até agora
            soma_qualidade += razao[i][1]  # Soma a qualidade dos primeiros k trabalhadores
            heapq.heappush(heap_maxima, -razao[i][1])  # Adiciona a qualidade à heap como negativa
        
        # Calculamos o custo inicial com os primeiros k trabalhadores
        custo_minimo = max_razao * soma_qualidade
        
        # Iteramos pelos trabalhadores restantes para encontrar o custo mínimo possível
        for i in range(k, len(qualidade)):
            max_razao = max(max_razao, razao[i][0])  # Atualiza a maior razão
            soma_qualidade += razao[i][1]  # Adiciona a qualidade do novo trabalhador
            soma_qualidade += heapq.heappop(heap_maxima)  # Remove a maior qualidade do heap
            heapq.heappush(heap_maxima, -razao[i][1])  # Adiciona a nova qualidade ao heap
            custo_minimo = min(custo_minimo, max_razao * soma_qualidade)  # Calcula o menor custo
        
        # Retorna o custo mínimo encontrado
        return custo_minimo
