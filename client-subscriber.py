
import socket

def run_client_subscriber(topic):
    subscriber_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    subscriber_socket.connect(('127.0.0.1', 5557))  
    print("Conectado ao servidor de assinatura")

    
    subscribe_command = f"SUBSCRIBE {topic}"
    subscriber_socket.send(subscribe_command.encode())
    print(f"Inscrito no tópico {topic}")

    while True:
        message = subscriber_socket.recv(1024).decode()
        if message:
            if message == "FINISH":
                break  
            print("Nova mensagem recebida:", message)

    subscriber_socket.close()

if __name__ == "__main__":
    topic = input("Digite o tópico para assinar: ")
    run_client_subscriber(topic)
=======
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
>>>>>>> 1ffeea308ac3a13b1bb8621c91c65f5ab8bc7452
