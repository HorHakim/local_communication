import socket


HOST = "0.0.0.0"   # écoute sur toutes les interfaces
PORT = 5000        # port choisi

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serveur en écoute sur le port {PORT}...")

    conn, addr = s.accept()
    with conn:
        print("Connecté par", addr)
        data = conn.recv(1024)
        print("Reçu :", data.decode())
        conn.sendall("Message bien reçu".format("utf-8"))
