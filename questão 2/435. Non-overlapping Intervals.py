from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervalos: List[List[int]]) -> int:
        # Ordena os intervalos com base no tempo de término (o segundo elemento de cada intervalo)
        intervalos.sort(key=lambda x: x[1])
        
        # Calcula o número total de intervalos
        total_intervalos = len(intervalos)
        
        # Inicializa o índice do último intervalo não sobreposto
        ultimo_intervalo = 0
        
        # Contador para o número de intervalos não sobrepostos
        contador_nao_sobrepostos = 1
        
        # Percorre os intervalos a partir do segundo
        for i in range(1, total_intervalos):
            # Verifica se o início do intervalo atual não se sobrepõe ao término do último intervalo selecionado
            if intervalos[i][0] >= intervalos[ultimo_intervalo][1]:
                ultimo_intervalo = i  # Atualiza o último intervalo não sobreposto
                contador_nao_sobrepostos += 1  # Incrementa o contador de intervalos não sobrepostos

        # Retorna o número de intervalos que precisam ser removidos
        return total_intervalos - contador_nao_sobrepostos
