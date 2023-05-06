"""Criar um programa receba um vetor de 100 posições, e divida em 4 partes. A primeira thread deve somar os elementos de 1 a 250

A segunda thread deve somar os elementos de 251 a 500 A terceira thread deve somar os elementos de 501 a 750 A quarta thread deve somar os elementos de 751 a 1000

Cada uma deve imprimir seu próprio resultado. E ao fim, o resultado final de todas as threads."""

#Aluno: Sebastião Oliveira Silva Neto - 2011478

import threading

vetor = list(range(1, 250))  # criando um vetor de 1 a 100
soma_total = 0  # inicializando a variável que irá armazenar a soma total

def soma_parte_vetor(inicio, fim):
    global soma_total
    soma = sum(vetor[inicio:fim])  # realizando a soma dos elementos da parte do vetor
    print(f"\n Soma da parte do vetor de {inicio+1} a {fim}: {soma}")  # imprimindo o resultado da soma da parte
    soma_total += soma  # somando a parte ao resultado total

# criando as threads para realizar a soma das partes do vetor
t1 = threading.Thread(target=soma_parte_vetor, args=(0, 25))
t2 = threading.Thread(target=soma_parte_vetor, args=(25, 50))
t3 = threading.Thread(target=soma_parte_vetor, args=(50, 75))
t4 = threading.Thread(target=soma_parte_vetor, args=(75, 100))
t5 = threading.Thread(target=soma_parte_vetor, args=(100, 250))

# iniciando as threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# esperando as threads terminarem
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(f"Soma total do vetor: {soma_total}")  # imprimindo o resultado da soma total