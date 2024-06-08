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

def run_each_component():
    "Function for running each component in a sequence."

    Elevator.serial_reset_position()

    sleep(3)

    Elevator.serial_command_up_1()

    sleep(3)

    ConveyorBelt.serial_command()

    sleep(9)

    Elevator.serial_command_down()

    sleep(5)
    
    Elevator.serial_command_up_3()
    
    Shelf.add_box(3)

    Pusher.serial_command_push()

    sleep(2)

    Pusher.serial_command_pull()

    sleep(2)

    Elevator.serial_command_down()

    sleep(5)

if __name__ == "__main__":

    # Create an instance of each component
    ConveyorBelt = ConveyorBelt()
    Elevator = Elevator()
    Pusher = Pusher()
    BoxQueue = BoxQueue()
    Stack = Stack()
    Shelf = Shelf() 

    print("Welcome to the box sorter!")

    #run_each_component() # For testing purposes

    while True:       
        command = -1

        # Await for sensor input
        with open("state.txt", "r") as f:
           command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
           if command_str:
                command = int(command_str)

        # Reset the state
        with open("state.txt", "w") as f:
       	    f.write("-1")

        # If there is a change in command, print it
        if command != -1:
            print(command)

        # If the elevator not in right position reset it
        if command == 0:
            Elevator.serial_reset_position()

        # If the command is 1, add a new box and put it in the right shelf
        # By concurrency, the command can also be 11
        elif command == 1 or command == "1" or command == 11 or command == "11":
            with open("state.txt", "w") as f:
       	        f.write("-2")
            
            # If a new box is detected, send this to virtual twin
            with open("send.txt", "w") as f:
                f.write("new box")
                   
            n = Shelf.next_floor() # Find the next empty floor, in the future this will be replaced by the input of the other group

            new_box = Box(box_id, 0)
            box_id += 1

            Elevator.serial_reset_position() # Reset the elevator position
            sleep(3)

            Elevator.serial_command_up_1() # Also the ideal position for the elevator to pick up the box
            sleep(3)

            ConveyorBelt.serial_command()
            sleep(9)

            if (n == 1):
                Shelf.add_box(n) # Then we only push the box onto the platform

            if (n == 2):
                Elevator.serial_command_down() # First go down and then go to the second floor
                sleep(5)

                Elevator.serial_command_up_2()
                Shelf.add_box(n)

            if (n == 3):
                Elevator.serial_command_down() # First go down and then go to the third floor
                sleep(5)

                Elevator.serial_command_up_3()
                Shelf.add_box(n)
            
            Pusher.serial_command_push() # Push the box to the shelf
            sleep(2)

            Pusher.serial_command_pull() # Retract the pusher
            sleep(2)

            Elevator.serial_command_down() # Go down to the ground floor
            sleep(5)
