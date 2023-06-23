import xmlrpc.server

def reverse_string(text):
    return text[::-1]

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_function(reverse_string, "reverse")
print("Servidor aguardando conexões...")
server.serve_forever()
