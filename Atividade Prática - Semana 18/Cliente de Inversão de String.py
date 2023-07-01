import Pyro4

uri = input("Digite o URI do servidor: ")
string_to_invert = input("Digite a string a ser invertida: ")

string_inverter = Pyro4.Proxy(uri)
inverted_string = string_inverter.invert_string(string_to_invert)

print("String invertida:", inverted_string)
