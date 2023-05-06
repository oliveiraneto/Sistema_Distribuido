import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor está escutando

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensagem = input('Digite uma mensagem para enviar ao servidor: ')
    s.sendall(mensagem.encode())
    print('Mensagem enviada para o servidor:', mensagem)
