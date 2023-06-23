from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(x, y):
    return x + y

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add_numbers, "add")
print("Servidor aguardando conexões...")
server.serve_forever()
