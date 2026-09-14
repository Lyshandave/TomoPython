import socket
import json

HOST = "127.0.0.1"
PORT = 5001

operation = input(
    "Operation (add/subtract/multiply/divide): "
).lower()

a = float(input("First number: "))
b = float(input("Second number: "))

request = {
    "operation": operation,
    "a": a,
    "b": b
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    client.sendall(
        json.dumps(request).encode("utf-8")
    )

    response = json.loads(
        client.recv(4096).decode("utf-8")
    )

print("Server response:", response)