from serial import send_command
from classes.BoxQueue import BoxQueue

class ConveyorBelt:
    def __init__(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value
        self.boxes = BoxQueue()
        

    def serial_command(self):
        send_command(self.motor_value, self.speed, self.duration)

    def print_boxes(self):
        self.boxes.print_boxes()
    
    def add_box(self, box):
        box.set_position(0)
        self.boxes.enqueue(box)