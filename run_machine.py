from classes.elevator import Elevator
from classes.pusher import Pusher
from classes.box import Box
from classes.BoxQueue import BoxQueue
from classes.ConveyorBelt import ConveyorBelt
from classes.stack import Stack
from classes.Shelf import Shelf
from time import sleep
from server import Client
import asyncio
import socket
import threading

def read_input() -> list:
    speed = int(input("Input speed: "))
    duration = int(input("Input duration: "))
    direction = int(input("Input direction: "))
    return [speed, duration, direction]

# List to store clients
clients = ["p"]

# Wait for new connections
def newConnections(socket):
    while True:
        sock, address = socket.accept()
        client = Client(sock, address, 1, "Name", True)
        client.start()
        clients.append(client)  # Add the client to the list

def run_each_component():
    if clients != []:
        #client = clients[0]
        #client.send_data("conveyor active")
        ConveyorBelt.serial_command(9000)

        sleep(1)

        Elevator.serial_command_up_3()

        sleep(1)

        Pusher.serial_command_push()

        sleep(1)

        Pusher.serial_command_pull()

        sleep(1)

        Elevator.serial_command_down()

        sleep(1)
    else:
        print("No clients connected.")


if __name__ == "__main__":

    #host = "localhost"
    #port = 5005
#
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.bind((host, port))
    #sock.listen(5)
#
    #newConnectionsThread = threading.Thread(target=newConnections, args=(sock,))
    #newConnectionsThread.start()

    ConveyorBelt = ConveyorBelt()
    Elevator = Elevator()
    Pusher = Pusher()
    BoxQueue = BoxQueue()
    Stack = Stack()
    Shelf = Shelf() 
    box_id = 0
    print("Welcome to the box sorter!")

    #run_each_component()

#    sock.close()
#    sys.exit(0)
    
    while True:
#       
        command = -1
        #await for sensor input
        with open("state.txt", "r") as f:
           command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
           if command_str:
                command = int(command_str)

        with open("state.txt", "w") as f:
       	    f.write("-1")
        if command != -1:
            print(command)
        #command = 0
        #command = int(input("ENTER COMMAND: "))
        if command == 0:
            Elevator.serial_reset_position()

        #sensor 1: move conveyor belt
        elif command == 1 or command == "1" or command == 11 or command == "11":
            n = int(input("Floor:"))
            n = Shelf.next_floor()
            Elevator.serial_reset_position()
            new_box = Box(box_id, 0)
            box_id += 1
            ConveyorBelt.add_box(new_box)
            Elevator.serial_reset_position()
            sleep(3)
            Elevator.serial_command_up_1()
            sleep(3)
            ConveyorBelt.serial_command()
            sleep(9)
            Elevator.serial_command_down()
            sleep(5)
            if (n == 1):
                Elevator.serial_command_up_1()
                Shelf.add_box(n)
            if (n == 2):
                Elevator.serial_command_up_2()
                Shelf.add_box(n)
            if (n == 3):
                Elevator.serial_command_up_3()
                Shelf.add_box(n)
            Pusher.serial_command_push()
            sleep(2)
            Pusher.serial_command_pull()
            sleep(2)
            Elevator.serial_command_down()
            sleep(5)

#        ConveyorBelt.print_boxes()
#        Elevator.print_boxes()
#        Pusher.print_boxes()
#        Shelf.print_boxes()
##
