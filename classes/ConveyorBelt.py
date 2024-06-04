from serial_motor import send_command
from classes.BoxQueue import BoxQueue

class ConveyorBelt:
    def __init__(self):
        self.boxes = BoxQueue()

    def serial_command(self, duration):
        send_command(4, 250, duration, 1)

    def print_boxes(self):
        if self.boxes.is_empty():
            print("Conveyor belt is empty")
        else:
            self.boxes.print_boxes()
    
    def add_box(self, box):
        box.set_location(0)
        self.boxes.enqueue(box)

    def remove_box(self):
        return self.boxes.dequeue()
