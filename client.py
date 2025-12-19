import socket
import os

from config import HOST, PORT



def send_text_to_server(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(text.encode("utf-8"))
        data = client_socket.recv(1024)

    print("Réponse du serveur :", data.decode())


if __name__ == "__main__":
    send_text_to_server("coucou")