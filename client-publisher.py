import socket

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 5557

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Escolhe a opção de Publisher
choice = 'publisher'
client_socket.sendall(choice.encode())

# Envia o tópico e a mensagem para o servidor
topic = input("Digite o tópico desejado: ")
client_socket.sendall(topic.encode())

message = input("Digite a mensagem a ser publicada: ")
client_socket.sendall(message.encode())

# Recebe a confirmação do servidor
response = client_socket.recv(1024).decode()
print("Resposta do servidor:", response)

# Fecha a conexão com o servidor
client_socket.close()

