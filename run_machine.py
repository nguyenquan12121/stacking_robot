"Logic for running the box sorter machine."

from classes.elevator import Elevator
from classes.pusher import Pusher
from classes.box import Box
from classes.BoxQueue import BoxQueue
from classes.ConveyorBelt import ConveyorBelt
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

def check_blockage():
    command = 0
    with open("state.txt", "r") as f:
        command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
        if command_str:
            command = int(command_str)
    while(command == 3):
        with open("state.txt", "r") as f:
            command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
            if command_str:
                command = int(command_str)
        print("Blockage detected")
    return

if __name__ == "__main__":

    # Create an instance of each component
    ConveyorBelt = ConveyorBelt()
    Elevator = Elevator()
    Pusher = Pusher()
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

            with open("color.txt", "r") as f: # Read the color of the box, which is detected by the other group
                color = f.read().strip()
                print(color)
            
            with open("color.txt", "w") as f:
                f.write("")
            
            if color == "red":
                n = 1
            elif color == "green":
                n = 2
            elif color == "blue":
                n = 3
            elif color == "":
                print("Box color not detected")
                print("Putting the box in the next free shelf")
                Shelf.next_floor()

            #new_box = Box(box_id, 0)
            #box_id += 1

            check_blockage()

            Elevator.serial_reset_position() # Reset the elevator position
            sleep(3)

            Elevator.serial_command_up_1() # Also the ideal position for the elevator to pick up the box
            sleep(3)

            check_blockage()

            ConveyorBelt.serial_command()
            sleep(9)

            #check if the box reached the pusher
            with open("state.txt", "r") as f:
                command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
                if command_str:
                    command = int(command_str)
            if command == 2:
                print("Box reached the pusher")
            else:
                while command != 2:
                    with open("state.txt", "r") as f:
                        command_str = f.read().strip()  # Read the value as a string and remove leading/trailing whitespace
                        if command_str:
                            command = int(command_str)
            check_blockage()

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
            
            check_blockage()
            Pusher.serial_command_push() # Push the box to the shelf
            sleep(2)
            check_blockage()
            Pusher.serial_command_pull() # Retract the pusher
            sleep(2)
            check_blockage()
            Elevator.serial_command_down() # Go down to the ground floor
            sleep(5)
