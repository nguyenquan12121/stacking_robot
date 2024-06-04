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
        #await for sensor input
        #with open("state.txt", "r") as f:
        #    command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
        #    if command_str:
        #        command = int(command_str)
#
        #with open("state.txt", "w") as f:
        #    f.write("-1")
 #       command = int(input("ENTER COMMAND: "))

        command = 0
        command = int(input("ENTER COMMAND: "))
        if command == -1:
            print("IDLING")
        elif command == 0:
            Elevator.serial_reset_position()
#
        #sensor 1: add to the conveyor belt
        elif command == 1:
            new_box = Box(box_id, 0)
            box_id += 1
            new_box.set_color("red")
            ConveyorBelt.add_box(new_box)
            ConveyorBelt.serial_command()
            # inputs = read_input()
            # ConveyorBelt.set_values(1, inputs[0], inputs[1],inputs[2])
            # ConveyorBelt.serial_command()
#
        #sensor 2: add to the elevator
        elif command == 2 and ConveyorBelt.boxes.is_empty() == False:
            if Elevator.box != None:
                print("Elevator is full")
                continue
            box = ConveyorBelt.remove_box()
            Elevator.add_box(box)
            match box.color:
                case "red":
                    Elevator.serial_command_up_1()
                case "green":
                    Elevator.serial_command_up_2()
                case "blue":
                    Elevator.serial_command_up_3()
                case _:
                    print("Invalid color")
            # inputs = read_input()
            # Elevator.set_values(2, inputs[0], inputs[1], inputs[2])
            # Elevator.serial_command()
        #sensor 3: add to the pusher
        elif command == 3 and Elevator.box != None:
            if Pusher.box != None:
                print("Pusher is full")
                continue
            box = Elevator.remove_box()
            Pusher.add_box(box)
            Pusher.serial_command_push()
            # inputs = read_input()
            # Pusher.set_values(3, inputs[0], inputs[1], inputs[2])
            # Pusher.serial_command()
        #sensor 4: add to the storage
        elif command == 4 and Pusher.box != None:
            box = Pusher.remove_box()
            Shelf.add_box(box)
            Pusher.serial_command_pull()
#
        # elevator goes down
        elif command == 5:  
            print("ELEVATOR GOING DOWN")
            Elevator.serial_command_down()

        ConveyorBelt.print_boxes()
        Elevator.print_boxes()
        Pusher.print_boxes()
        Shelf.print_boxes()
#
