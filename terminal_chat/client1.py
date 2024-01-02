import socket

HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
BYTESIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_IP, PORT))

while True:
    message = client.recv(BYTESIZE).decode()

    if message.capitalize() == "Done":
        print("Good Bye!\n")
        client.close()
        break
    print(message)
    message = input("Enter Message: ")
    client.send(message.encode())
