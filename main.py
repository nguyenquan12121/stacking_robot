from classes.elevator import Elevator
from classes.pusher import Pusher
from classes.box import Box
from classes.BoxQueue import BoxQueue
from classes.ConveyorBelt import ConveyorBelt
from classes.stack import Stack

from time import sleep

#speed, duration, motor_value
ConveyorBelt = ConveyorBelt(240, 5000, 1)
Elevator = Elevator(240, 4000, 2)
Pusher = Pusher(240, 3000, 3)
BoxQueue = BoxQueue()
Stack = Stack()

testbox = Box(1, 0)
box_id = 0

print("Welcome to the box sorter!")

while True:
    #await for sensor input
    command = int(input("1, 2, 3, 4: for the sensors:"))

    #sensor 1: add to the conveyor belt
    if command == 1:
        new_box = Box(box_id, 0)
        box_id += 1
        ConveyorBelt.add_box(new_box)
        ConveyorBelt.serial_command()

    #sensor 2: add to the elevator
    elif command == 2 and ConveyorBelt.boxes.is_empty() == False:
        if Elevator.box != None:
            print("Elevator is full")
            continue
        box = ConveyorBelt.remove_box()
        Elevator.add_box(box)
        Elevator.serial_command()
    #sensor 3: add to the pusher
    elif command == 3 and Elevator.box != None:
        if Pusher.box != None:
            print("Pusher is full")
            continue
        box = Elevator.remove_box()
        Pusher.add_box(box)
        Pusher.serial_command()
    #sensor 4: add to the storage
    elif command == 4 and Pusher.box != None:
        box = Pusher.remove_box()
        Stack.add_box(box)

    ConveyorBelt.print_boxes()
    Elevator.print_boxes()
    Pusher.print_boxes()
    Stack.print_boxes()

    #speed, duration, motor_value
#    ConveyorBelt.set_values(1000, 50, 1)
#
#    #set value to time for elevator to reach the top
#    Elevator.set_values(20, 20, 2)
#
#    #set value to time for pusher to push the box
#    Pusher.set_values(20, 20, 3)
#
