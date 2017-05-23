import socket
import ssl

host = 'localhost'
port = 46143

new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = ssl.wrap_socket(new_socket)
connection.connect((host, port))

while True:

    command = raw_input('Input data to send to the server:')

    print('Sending command to server:')
    print(command)

    connection.sendall(command)

    if command == 'Close Connection':
        connection.close()
        break

    elif command == 'Shutdown':
        connection.close()
        exit()