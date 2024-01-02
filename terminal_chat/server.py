import socket

HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
BYTESIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST_IP, PORT))
server.listen()

print("Running!\n")
client, server_socket = server.accept()
client.send("Welcome!\n".encode())

while True:
    message = client.recv(BYTESIZE).decode()

    if message.capitalize() == "Done":
        print("Good Bye!\n")
        client.send(message.encode())
        server.close()
        break
    print(message)
    message = input("Enter Message: ")
    client.send(message.encode())
