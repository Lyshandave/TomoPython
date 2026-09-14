import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    print("Connected to server.")
    print("Type exit to close the connection.")

    while True:
        message = input("Message: ")

        client.sendall(message.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")

        print("Server response:", response)

        if message.lower() == "exit":
            break

print("Client stopped.")