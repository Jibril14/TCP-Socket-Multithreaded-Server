import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 54321))
payload = "Mr Abdullahi Abdulwasiu"

try:
    while True:
        client_socket.send(payload.encode("utf-8"))
        data = client_socket.recv(1024)
        print(str(data))
        more = input("Enter more data? Type 'yes': ")
        if more.lower() == "yes":
            payload = input("Enter Payload:")
        else:
            break

except KeyboardInterrupt:
    print("Exited by user")
client_socket.close()