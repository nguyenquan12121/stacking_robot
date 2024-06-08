import socket
import sys

host = "192.168.67.239"
port = 123

# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

def send_message(message):
    "Sends a message to the server its connected to."

    if message != "red" or message != "green" or message != "blue":
        print("Invalid message")
        return
        
    print(f"Sending: {message}")
    sock.sendall(str.encode(message))