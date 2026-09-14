import socket
import json

HOST = "127.0.0.1"
PORT = 5001


def calculate(request):
    operation = request.get("operation")
    a = request.get("a")
    b = request.get("b")

    try:
        if operation == "add":
            result = a + b

        elif operation == "subtract":
            result = a - b

        elif operation == "multiply":
            result = a * b

        elif operation == "divide":
            if b == 0:
                return {
                    "status": "error",
                    "message": "Division by zero."
                }

            result = a / b

        else:
            return {
                "status": "error",
                "message": "Unknown operation."
            }

        return {
            "status": "success",
            "result": result
        }

    except (TypeError, ValueError):
        return {
            "status": "error",
            "message": "Invalid values."
        }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Calculator server listening on {HOST}:{PORT}")

    while True:
        connection, address = server.accept()

        with connection:
            print("Client connected:", address)

            data = connection.recv(4096)

            if data:
                request = json.loads(data.decode("utf-8"))

                response = calculate(request)

                connection.sendall(
                    json.dumps(response).encode("utf-8")
                )