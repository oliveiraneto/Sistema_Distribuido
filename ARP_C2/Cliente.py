import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Definir o protocolo de comunicação
# O protocolo consiste em mensagens no formato "tipo|dados"
# O tipo pode ser "MSG" para mensagens de texto ou "FILE" para arquivos
# Os dados podem ser uma mensagem de texto ou o nome do arquivo
def receive_message(s):
    data = s.recv(1024).decode()
    parts = data.split('|')
    return parts[0], parts[1]

def send_message(s, type, data):
    data = f"{type}|{data}".encode()
    s.sendall(data)

def send_file(s, filename):
    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            s.sendall(data)
            data = f.read(1024)

def receive_file(s, filename):
    with open(filename, 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Enviar uma mensagem de texto
    send_message(s, 'MSG', 'Hello, world')
    # Receber a mensagem de resposta
    type, data = receive_message(s)
    if type == 'MSG':
        print(f'Mensagem ecoada: {data}')
    else:
        print(f'Tipo de mensagem inválido: {type}')
    # Enviar um arquivo
    send_message(s, 'FILE', 'example.txt')
    send_file(s, 'example.txt')
    # Receber a mensagem de resposta
    type, data = receive_message(s)
    if type == 'MSG':
        print(f'Mensagem ecoada: {data}')
    else:
        print(f'Tipo de mensagem inválido: {type}')
