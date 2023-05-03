"""Implemente um programa em Python que realize o cálculo das somas dos valores das linhas de uma matriz 5x5 de números inteiros e imprima o resultado na tela. 
O cálculo do somatório de cada linha deve ser realizado em paralelo por threads. """

import threading

# Definindo a matriz 5x5
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Função que calcula a soma de uma linha da matriz
def sum_row(row):
    return sum(row)

# Lista para armazenar os resultados das somas
results = []

# Criando as threads para calcular as somas das linhas
for row in matrix:
    t = threading.Thread(target=sum_row, args=(row,))
    t.start()
    results.append(t)

# Aguardando todas as threads terminarem
for t in results:
    t.join()

# Imprimindo os resultados das somas
for i, t in enumerate(results):
    print(f"Soma da linha {i+1}: {t.result()}")
