import socket 

CLIENT = "0.0.0.0"
PORT = 6060

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((CLIENT, PORT))

print("terhubung ke server...")
print("ketik exit untuk keluar")

while True: 
    pesan = input("Kamu: ")

    if pesan.lower() == "exit": 
        break 

    client.send(pesan.encode())

    data = client.recv(1024)

    print("Server: ", data.decode())

client.close()
print("Koneksi tertutup")