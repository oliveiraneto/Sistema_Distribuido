import socket

# Configuração do endereço e porta multicast
multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Criação do socket multicast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configuração do socket para multicast
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

# Associação do socket ao endereço e porta do servidor
sock.bind(server_address)

# Loop infinito para receber e processar as mensagens dos clientes
while True:
    print('\nAguardando mensagem dos clientes...')
    data, address = sock.recvfrom(1024)

    # Inverte a string recebida
    message = data.decode()[::-1]

    # Envia a mensagem invertida de volta para o cliente
    print(f'Recebido "{data.decode()}" de {address}. Enviando "{message}" de volta...')
    sent = sock.sendto(message.encode(), address)
