import socket

def main():
    # Cria um socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Vincula o socket a um endereço e porta
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print("Servidor pronto para receber mensagens...")

    while True:
        # Recebe a mensagem do cliente
        data, client_address = server_socket.recvfrom(1024)

        # Inverte a string
        inverted_data = data.decode('utf-8')[::-1]

        # Envia a string invertida de volta ao cliente
        server_socket.sendto(inverted_data.encode('utf-8'), client_address)

if __name__ == "__main__":
    main()
