import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor irá escutar

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Servidor aguardando conexão...')
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Mensagem recebida do cliente:', data.decode())
