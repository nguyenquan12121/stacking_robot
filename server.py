import socket
import threading
from time import sleep

#Variables for holding information about connections
connections = []
total_connections = 0

#Client class, new instance created for each connected client
#Each instance has the socket and address that is associated with items
#Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    "Client class for handling each connected client. Each client has a unique ID and name. The client can send and receive data."

    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        send_data_thread = threading.Thread(target = self.send_data) # Create new thread for sending data
        send_data_thread.start()
        
    
    def __str__(self):
        return str(self.id) + " " + str(self.address)
    
    #Attempt to get data from client
    #If unable to, assume client has disconnected and remove him from server data
    #If able to and we get data back, print it in the server and send it back to every
    #client aside from the client that has sent it
    #.decode is used to convert the byte data into a printable string
    def run(self):
        "Function for receiving data from the client and sending it to all other clients."
        while self.signal:
            try:
                data = self.socket.recv(32)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                connections.remove(self)
                break
            
            # If data is received, print it and write it to state.txt
            # Used in run_machine.py to control the machine components
            if data != "":
                result = str(data.decode("utf-8"))

                if result == "green" or result == "red" or result == "blue" :
                    with open("color.txt", "w") as f:
                        f.write(str(result))
                else:
                    s = ""
                    with open("state.txt", "r") as f:
                        s = f.read(str(result))
                        print(s)
                    if s != "-2":
                        with open("state.txt", "w") as f:
                            f.write(result)
                        
                print("ID " + str(self.id) + ": " + str(data.decode("utf-8")))


    def send_data(self):
        "Function for sending data to the client"
        
        # idea: If something is written to send.txt then this content is send to the client
        while True:
            with open("send.txt", "r") as f:
                data = f.read()
                if data:
                    try:
                        self.socket.sendall(str.encode(data))
                    except:
                        print("Error sending data")
                    with open("send.txt", "w") as f:
                        f.write("")
            sleep(1)
            


def newConnections(socket):
    "Function for handling new connections to the server"    
    
    while True:
        sock, address = socket.accept() # Accept new connection
        global total_connections
        connections.append(Client(sock, address, total_connections, "Name", True)) # Create new client instance
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        total_connections += 1

if __name__ == "__main__":
    # Get host and port
    host = input("Host: ") # The server's hostname or IP address (Pi itself)
    port = int(input("Port: "))

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    # Create new thread to wait for connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()
    newConnectionsThread.join() 
