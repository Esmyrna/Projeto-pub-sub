import socket
import threading

# Dicionário para armazenar os tópicos e as mensagens
topics = {}

# Função para lidar com as conexões dos clientes
def handle_client(connection, address):
    print(f"Cliente {address} conectado.")

    # Recebe a escolha do cliente: Publisher ou Subscriber
    choice = connection.recv(1024).decode()
    print(f"Cliente {address} escolheu: {choice}")

    if choice == 'publisher':
        # Recebe o tópico e a mensagem do Publisher
        topic = connection.recv(1024).decode()
        message = connection.recv(1024).decode()
        print(f"Cliente {address} publicou a mensagem '{message}' no tópico '{topic}'")

        # Armazena a mensagem no tópico correspondente
        if topic in topics:
            topics[topic].append(message)
        else:
            topics[topic] = [message]

        # Envia uma confirmação ao Publisher
        response = "Mensagem publicada com sucesso."
        connection.sendall(response.encode())
    elif choice == 'subscriber':
        # Recebe o tópico escolhido pelo Subscriber
        topic = connection.recv(1024).decode()
        print(f"Cliente {address} se inscreveu no tópico '{topic}'")

        # Verifica se o tópico existe
        if topic in topics:
            # Envia as mensagens correspondentes ao tópico para o Subscriber
            messages = topics[topic]
            for message in messages:
                connection.sendall(message.encode())
        else:
            response = "Tópico não encontrado."
            connection.sendall(response.encode())

    print(f"Cliente {address} desconectado.")
    connection.close()

# Função para remover os tópicos sem clientes
def remove_inactive_topics():
    while True:
        # Remove os tópicos sem clientes
        inactive_topics = [topic for topic in topics if not topics[topic]]
        for topic in inactive_topics:
            del topics[topic]
        
        # Aguarda um curto período de tempo antes de verificar novamente
        # isso evita que a iteração ocorra ao mesmo tempo que o dicionário é modificado
        threading.Event().wait(1)

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 5557

# Criação do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("Servidor iniciado.")

# Thread para remover os tópicos sem clientes
cleanup_thread = threading.Thread(target=remove_inactive_topics)
cleanup_thread.start()

# Aceita as conexões dos clientes em uma thread separada
while True:
    connection, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection, address))
    client_thread.start()
