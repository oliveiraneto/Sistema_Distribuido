"""Implemente um programa em Python que multiplique os elementos de um vetor de tamanho 1000 por um escalar e depois imprima o vetor resultante na tela. 
O processo de multiplicação deve ser realizado em paralelo por 10 threads, onde cada thread deve ser responsável por multiplicar 100 elementos do vetor pelo escalar. """

import threading

# Definindo o vetor de tamanho 1000
vetor = [i for i in range(1000)]

# Definindo o escalar
escalar = 2

# Função que multiplica os elementos do vetor por um escalar
def multiply(start, end):
    for i in range(start, end):
        vetor[i] *= escalar

# Lista para armazenar as threads
threads = []

# Criando as threads para multiplicar os elementos do vetor
for i in range(0, 1000, 100):
    t = threading.Thread(target=multiply, args=(i, i+100))
    t.start()
    threads.append(t)

# Aguardando todas as threads terminarem
for t in threads:
    t.join()

# Imprimindo o vetor resultante
print(vetor)
