import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:8000")
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
result = client.add(x, y)
print("Resultado da soma:", result)
