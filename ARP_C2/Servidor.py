import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Definir o protocolo de comunicação
# O protocolo consiste em mensagens no formato "tipo|dados"
# O tipo pode ser "MSG" para mensagens de texto ou "FILE" para arquivos
# Os dados podem ser uma mensagem de texto ou o nome do arquivo
def receive_message(conn):
    data = conn.recv(1024).decode()
    parts = data.split('|')
    return parts[0], parts[1]

def send_message(conn, message):
    data = f"MSG|{message}".encode()
    conn.sendall(data)

def receive_file(conn, filename):
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

def send_file(conn, filename):
    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            conn.sendall(data)
            data = f.read(1024)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Servidor aguardando conexões...')
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            # Receber a mensagem do cliente
            type, data = receive_message(conn)
            if type == 'MSG':
                print(f'Mensagem recebida: {data}')
                # Enviar uma mensagem de resposta
                send_message(conn, f'Recebido: {data}')
            elif type == 'FILE':
                print(f'Arquivo recebido: {data}')
                # Salvar o arquivo recebido
                receive_file(conn, data)
                # Enviar uma mensagem de resposta
                send_message(conn, f'Recebido: {data}')
            else:
                print(f'Tipo de mensagem inválido: {type}')
                # Enviar uma mensagem de erro
                send_message(conn, f'Erro: tipo de mensagem inválido')
