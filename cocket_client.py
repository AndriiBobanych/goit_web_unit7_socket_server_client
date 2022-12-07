import socket
from datetime import datetime


def run_client():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5050

    socket_client = socket.socket()
    socket_client.connect((host, port))

    try:
        message_to_server = "Hello Server! Let's start?"
        socket_client.send(message_to_server.encode())
        print(f"Client's message 'Hello Server! Let's start?' was sent to Server at {datetime.now()}")
        message_from_server = socket_client.recv(1024).decode()
        print(f"Received message '{message_from_server}' from Server at {datetime.now()}")

        while True:
            message_to_server = input(">>> ").lower().strip()

            if message_to_server != "exit":
                socket_client.send(message_to_server.encode())
                print(f"Client's message '{message_to_server}' was sent to Server at {datetime.now()}")
            else:
                break

            message_from_server = socket_client.recv(1024).decode()
            print(f"Received message '{message_from_server}' from Server at {datetime.now()}")

    except KeyboardInterrupt:
        print("Client was interrupted")
    finally:
        socket_client.close()
        print("Client socket was closed")


if __name__ == '__main__':
    run_client()


"""
Client's message 'Hello Server! Let's start?' was sent to Server at 2022-12-07 23:58:32.372694
Received message 'Hello Client! OK' from Server at 2022-12-07 23:58:32.372694
>>> print something
Client's message 'print something' was sent to Server at 2022-12-07 23:58:52.077419
Received message 'received. printed. sent.' from Server at 2022-12-07 23:59:14.059827
>>> nice job
Client's message 'nice job' was sent to Server at 2022-12-07 23:59:33.601073
Received message 'thanks' from Server at 2022-12-07 23:59:40.470653
>>> exit
Client socket was closed

Process finished with exit code 0
"""
