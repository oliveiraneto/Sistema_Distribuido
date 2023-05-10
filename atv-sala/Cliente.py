import socket

def main():
    # Cria um socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define o endereço e a porta do servidor
    server_address = ('localhost', 12345)

    while True:
        # Solicita a mensagem do usuário
        message = input("Digite a mensagem a ser invertida (digite 'sair' para encerrar): ")

        if message.lower() == 'sair':
            break

        # Envia a mensagem ao servidor
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Recebe a mensagem invertida do servidor
        inverted_message, _ = client_socket.recvfrom(1024)
        print("Mensagem invertida:", inverted_message.decode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()
