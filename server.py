import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.topics = {}

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Servidor iniciado em {self.host}:{self.port}")

        while True:
            client_socket, address = self.socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        topic = client_socket.recv(1024).decode()
        is_publisher = client_socket.recv(1024).decode() == "publisher"

        if topic not in self.topics:
            self.topics[topic] = []

        if is_publisher:
            self.topics[topic].append(client_socket)
            print(f"Novo publicador conectado ao tópico '{topic}'")
        else:
            self.topics[topic].append(client_socket)
            print(f"Novo assinante conectado ao tópico '{topic}'")

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    self.topics[topic].remove(client_socket)
                    print(f"Cliente desconectado do tópico '{topic}'")
                    break

                self.send_message_to_subscribers(topic, message)
            except ConnectionResetError:
                self.topics[topic].remove(client_socket)
                print(f"Cliente desconectado do tópico '{topic}'")
                break

    def send_message_to_subscribers(self, topic, message):
        subscribers = self.topics[topic].copy()
        for subscriber in subscribers:
            try:
                subscriber.send(message.encode())
            except ConnectionResetError:
                self.topics[topic].remove(subscriber)
                print(f"Cliente desconectado do tópico '{topic}'")

if __name__ == "__main__":
    server = Server("localhost", 8000)
    server.start()
