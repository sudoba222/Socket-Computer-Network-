import socket
import random


server_name = "Server "
host = "127.0.0.1"
port = 5005


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server is waiting for a client...")

while True:

    connection, address = server_socket.accept()
    print("Action: Connection accepted from", address)


    data = connection.recv(1024).decode()
    if not data:
        break


    parts = data.split(",")
    client_name = parts[0]
    client_num = int(parts[1])


    if client_num < 1 or client_num > 100:
        print("Action: Number out of range. Shutting down server.")
        connection.close()
        break


    server_num = random.randint(1, 100)
    total_sum = client_num + server_num


    print("Client Name:", client_name)
    print("Server Name:", server_name)
    print("Client Number:", client_num)
    print("Server Number:", server_num)
    print("The Sum is:", total_sum)


    response = server_name + "," + str(server_num)
    connection.send(response.encode())
    print("Action: Response sent to client.")

    connection.close()


server_socket.close()
print("Action: Server socket closed.")