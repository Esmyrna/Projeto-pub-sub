import socket

# Configurações do cliente
HOST = 'localhost'
PORT = 5000

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Escolhe a opção de Subscriber
choice = 'subscriber'
client_socket.sendall(choice.encode())

# Escolhe o tópico a ser assinado
topic = input("Digite o tópico desejado: ")
client_socket.sendall(topic.encode())

# Recebe as mensagens correspondentes ao tópico do servidor
while True:
    message = client_socket.recv(1024).decode()
    if not message:
        break
    print("Nova mensagem recebida:", message)

# Fecha a conexão com o servidor
client_socket.close()
