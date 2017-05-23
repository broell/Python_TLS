import socket
import ssl

host = 'localhost'
port = 46143

bind_socket = socket.socket()
bind_socket.bind((host, port))
bind_socket.listen(5)


def communicate(connection):

    command = connection.read()

    while command:
        if command == 'Close Connection':
            connection.close()
            break

        elif command == 'Shutdown':
            connection.close()
            exit()

        else:
            print(command)


while True:
    new_socket, remote_address = bind_socket.accept()

    # openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem
    connection = ssl.wrap_socket(new_socket, server_side=True, certfile="cert.pem", ssl_version=ssl.PROTOCOL_TLSv1)

    communicate(connection)
