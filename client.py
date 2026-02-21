import socket


client_name = "Client"
host = "127.0.0.1"
port = 5005


number = int(input("Enter an integer between 1 and 100: "))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Action: Attempting to connect to server...")
client_socket.connect((host, port))


message = client_name + "," + str(number)
client_socket.send(message.encode())
print("Action: Message sent to server.")


reply = client_socket.recv(1024).decode()
reply_parts = reply.split(",")
server_name = reply_parts[0]
server_num = int(reply_parts[1])


print("My Name:", client_name)
print("Server Name:", server_name)
print("My Number:", number)
print("Server Number:", server_num)
print("Total Sum:", (number + server_num))


client_socket.close()
print(" Client socket closed")