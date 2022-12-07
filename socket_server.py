import socket
from datetime import datetime


def run_server():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5050

    socket_server = socket.socket()
    socket_server.bind((host, port))
    socket_server.listen(1)
    connection, address = socket_server.accept()

    try:
        message_from_client = connection.recv(1024).decode()
        print(f"Received message '{message_from_client}' from Client at {datetime.now()}")
        connection.send("Hello Client! OK".encode())
        print(f"Server's message 'Hello Client! OK' was sent to Client at {datetime.now()}")

        while True:

            message_from_client = connection.recv(1024).decode()
            print(f"Received message '{message_from_client}' from Client at {datetime.now()}")

            if not message_from_client:
                break

            message_to_client = input(">>> ").lower().strip()
            connection.send(message_to_client.encode())
            print(f"Server's message '{message_to_client}' was sent to Client at {datetime.now()}")

    except KeyboardInterrupt:
        print("Server was interrupted")
    finally:
        connection.close()
        print("Server socket was closed")


if __name__ == '__main__':
    run_server()


"""
Received message 'Hello Server! Let's start?' from Client at 2022-12-07 23:58:32.372694
Server's message 'Hello Client! OK' was sent to Client at 2022-12-07 23:58:32.372694
Received message 'print something' from Client at 2022-12-07 23:58:52.077419
>>> received. printed. sent.
Server's message 'received. printed. sent.' was sent to Client at 2022-12-07 23:59:14.059827
Received message 'nice job' from Client at 2022-12-07 23:59:33.601073
>>> thanks
Server's message 'thanks' was sent to Client at 2022-12-07 23:59:40.470653
Received message '' from Client at 2022-12-07 23:59:47.599619
Server socket was closed

Process finished with exit code 0
"""
