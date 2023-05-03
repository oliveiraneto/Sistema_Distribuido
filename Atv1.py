"""Escreva um programa em Python composto por duas threads: a primeira deve contar e exibir na tela todos os números entre 1 e 500 (de forma crescente); 
a segunda deve contar e exibir na tela todos os números entre 500 e 1 (de forma decrescente). As duas threads devem ser executadas em paralelo."""

import threading

def count_up():
    for i in range(1, 501):
        print(i)

def count_down():
    for i in range(500, 0, -1):
        print(i)

if __name__ == "__main__":
    t1 = threading.Thread(target=count_up)
    t2 = threading.Thread(target=count_down)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
