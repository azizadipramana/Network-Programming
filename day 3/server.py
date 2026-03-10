import socket 
import threading

SERVER = "10.28.74.102"
PORT = 6060

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((SERVER, PORT))
server.listen(1)

print("Server sedang berjalan...")

def handle_client(conn, addr): 
    print(f"Client terhubung: {addr}")

    while True: 
        try: 
            data = conn.recv(1024)
            if not data: 
                break 

            pesan = data.decode()
            print(f"{addr}: {pesan}")

            conn.send("Pesan diterima server".encode())

            if pesan.lower() == "exit": 
                print(f"Client {addr} disconnect")
                break 
            
            pesan = input("Server: ")
            if pesan.lower() == "stop": 
                print("All service is closed")
                break 
        
        except: 
            break

    conn.close()
    print(f"Client {addr} disconnect")

while True: 
    conn, addr = server.accept()

    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

    print("Jumlah client:", threading.active_count() - 1)
    