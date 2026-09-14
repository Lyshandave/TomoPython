import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    connection, address = server.accept()

    with connection:
        print("Connected by:", address)

        while True:
            data = connection.recv(1024)

            if not data:
                break

            message = data.decode("utf-8")
            print("Client:", message)

            if message.lower() == "exit":
                connection.sendall(b"Connection closed by server.")
                break

            response = f"Server received: {message}"
            connection.sendall(response.encode("utf-8"))

print("Server stopped.")