import socket 

CLIENT = "10.28.74.102"
PORT = 6060

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((CLIENT, PORT))

client.send("Halo Server sayang".encode())

data = client.recv(1024)

print("Balasan Server:", data.decode())

client.close()