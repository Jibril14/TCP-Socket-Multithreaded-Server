import socket
import sys
import threading

# specify host, port and initaial Thread
# get the hostname dynamically
host = socket.gethostbyname(socket.gethostname())
port = 54321
thread_count = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # bind host address and port together
    server_socket.bind((host, port))

except socket.error as err:
    # if any error occurs then with the
    # help of sys.exit() exit from the program
    print("Error Code: " + str(err))
    sys.exit()

# socket binding operation completed
print("socket binding operation completed")


def handle_client(conn, addr):
    print("connection from " + addr[0] + " on Port " + str(addr[1]))
    while True:
        # receive data stream. it won't accept data packet greater than 1024
        # bytes
        data = conn.recv(1024).decode("utf-8")
        if data.isdigit():
            reply = "Server accept string values only"
        else:
            reply = f"Server received: '{data}'"

        if not data:
            # if data is not received break
            break
        conn.send(str.encode(reply))
    conn.close()


def start():
    server_socket.listen()  # configure how many client the server can listen simultaneously

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        thread_count = threading.activeCount() - 1
        print("Number of client connected now " + str(thread_count))


print("Waiting for connection...")
start()
