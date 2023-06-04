import socket

def subscriber():
    host = "localhost"
    port = 8000

    topic = input("Digite o tópico: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(topic.encode())
    client_socket.send("subscriber".encode())

    while True:
        message = client_socket.recv(1024).decode()
        print(f"Mensagem recebida: {message}")

    client_socket.close()

if __name__ == "__main__":
    subscriber()
