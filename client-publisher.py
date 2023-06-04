import socket

def publisher():
    host = "localhost"
    port = 8000

    topic = input("Digite o tópico: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(topic.encode())
    client_socket.send("publisher".encode())

    while True:
        message = input("Digite a mensagem: ")
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    publisher()
