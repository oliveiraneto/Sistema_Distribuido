import Pyro4

uri = input("Digite o URI do servidor: ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

number_adder = Pyro4.Proxy(uri)
result = number_adder.add_numbers(num1, num2)

print("Resultado da soma:", result)
