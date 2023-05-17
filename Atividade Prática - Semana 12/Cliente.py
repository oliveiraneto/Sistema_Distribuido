import socket

# Configuração do endereço e porta multicast
multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Criação do socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configuração do socket para multicast
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

# Mensagem a ser enviada para o servidor
message = input('Digite a mensagem a ser invertida: ')

# Envia a mensagem para o servidor
print(f'Enviando "{message}" para o servidor...')
sent = sock.sendto(message.encode(), server_address)

# Recebe a mensagem invertida do servidor
data, server = sock.recvfrom(1024)
print(f'Recebido "{data.decode()}" de {server}.')
