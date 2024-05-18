from classes.Elevator import Elevator
from classes.Pusher import Pusher
from classes.Box import Box
from classes.BoxQueue import BoxQueue
from classes.ConveyorBelt import ConveyorBelt
from classes.Stack import Stack

from serial import send_command
from time import sleep

#speed, duration, motor_value, boxes
ConveyorBelt = ConveyorBelt(100, 50, 1)
Elevator = Elevator(100, 50, 2)
Pusher = Pusher(100, 50, 3)
BoxQueue = BoxQueue()
Stack = Stack()


testbox = Box(1, 0)

print("Welcome to the box sorter!")

while True:
    sleep(1)
    ConveyorBelt.add_box(testbox)
    ConveyorBelt.print_boxes()
    sleep(1)
    #remove the box from the conveyor belt
    #add to the elevator    
    Elevator.add_box(testbox)
    Elevator.print_boxes()
    sleep(1)
    #remove the box from the elevator
    #add to the pusher
    Pusher.add_box(testbox)
    Pusher.print_boxes()
    sleep(1)
    #remove the box from the pusher
    #add to the storage
    Stack.add_box(testbox)
    Stack.print_boxes()
    sleep(1)



