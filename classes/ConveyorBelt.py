from serial_motor import send_command
from classes.BoxQueue import BoxQueue

class ConveyorBelt:
    def __init__(self):
        self.boxes = BoxQueue()

    def serial_command(self, duration = 9000):
        "Send command to the conveyor belt motor."

        with open("send.txt", "w") as f:
            f.write("conveyor active")
        send_command(4, 250, duration, 1)

    def print_boxes(self):
        "Print the boxes on the conveyor belt."

        if self.boxes.is_empty():
            print("Conveyor belt is empty")
        else:
            self.boxes.print_boxes()
    
    def add_box(self, box):
        "Add a box to the conveyor belt."

        box.set_location(0)
        self.boxes.enqueue(box)

    def remove_box(self):
        "Remove a box from the conveyor belt."
        return self.boxes.dequeue()
