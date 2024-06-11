import socket
import threading
import sys
from client.communicate import Communicate

# Wait for incoming data from server
# .decode is used to turn the message in bytes to a string
def receive(socket, signal):
    "Function for receiving data from the server"
    c = Communicate()

    while signal:
        try:
            data = socket.recv(32)
            print("Send to unity: ")
            print(str(data.decode("utf-8")))

            c.send_data(str(data.decode("utf-8")))

        except:
            print("You have been disconnected from the server")
            signal = False
            break

# # Set up server connection
# host = "192.168.67.239"
# port = 123

<<<<<<< HEAD
# # Attempt connection to server
# try:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect((host, port))
# except:
#     print("Could not make a connection to the server")
#     input("Press enter to quit")
#     sys.exit(0)
=======
# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    # input("Press enter to quit")
    # sys.exit(0)
>>>>>>> 608e94424edd7cc384785474874fed8a6e327acf

# # Create new thread to wait for data
# receiveThread = threading.Thread(target = receive, args = (sock, True))
# receiveThread.start()

def send_message(message):
    "Sends a message to the server its connected to."
    print(f"Value: {message}")
<<<<<<< HEAD
    #sock.sendall(str.encode(message))
=======
    try:
        sock.sendall(str.encode(message))
    except:
        raise Exception()    
>>>>>>> 608e94424edd7cc384785474874fed8a6e327acf
