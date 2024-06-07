import socket
import threading
import sys
from communicate import Communicate


# def unity_action(data):
#     if (data == "conveyor active" or data == "conveyor disable" or data == "elevator 1" or data == "elevator 2" or 
#         data == "elevator 3" or data == "elevator down" or data == "pusher out" or data == "pusher in" ):
#         Communicate.send_data("data")

#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    c = Communicate()

    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))

            c.send_data(str(data.decode("utf-8")))

        except:
            print("You have been disconnected from the server")
            signal = False
            break

#Get host and port
# host = input("Host: ")
# port = int(input("Port: "))

host = "192.168.67.239"
port = 123

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

def send_message(message):
    print(f"Value: {message}")
    sock.sendall(str.encode(message))
