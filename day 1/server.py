import socket

SERVER = "10.28.74.102"
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen(1)

print("Server menunggu koneksi....")

conn, addr = server.accept()

print("Terhubung dengan", addr)

data = conn.recv(1024)

print("Pesan dari client:", data.decode())

conn.send("Halo client".encode())

conn.close()