import socket
import os

from config import HOST, PORT



def send_text_to_server(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_object:
        socket_object.connect((HOST, PORT))
        socket_object.sendall(text.encode("utf-8"))
        data = socket_object.recv(1024)

    print("Réponse du serveur :", data.decode())


if __name__ == "__main__":
    send_text_to_server("coucou")