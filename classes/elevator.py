from serial_motor import send_command
from time import sleep

class Elevator:
    "Elevator class for handling the elevator. The elevator can move up and down and hold a box."

    def __init__(self):
        self.box = None
        self.pos = 0

    def serial_command_up_3(self):
        "Send command to the elevator motor to move up to the third floor."

        with open("send.txt", "w") as f:
            f.write("elevator 3")

        sleep(2)
        send_command(2, 250, 9000, 1)
        sleep(9)
        send_command(2, 250, 9000, 1)
        sleep(3)
        self.pos = 3

    def serial_command_up_2(self):
        "Send command to the elevator motor to move up to the second floor."

        with open("send.txt", "w") as f:
            f.write("elevator 2")

        sleep(2)
        send_command(2, 250, 9000, 1)
        sleep(6)
        self.pos = 2
    
    def serial_command_up_1(self):
        "Send command to the elevator motor to move up to the first floor."

        with open("send.txt", "w") as f:
            f.write("elevator 1")
        sleep(2)
        send_command(2, 250, 2000, 1)
        sleep(2)
        self.pos = 1
    
    def serial_command_down(self):
        "Send command to the elevator motor to move down."

        with open("send.txt", "w") as f:
            f.write("elevator down")
            
        if (self.pos == 3):
            send_command(2, 250, 5000, 2)
        
        if (self.pos == 2):
            send_command(2, 250, 4000, 2)

        if (self.pos == 1):
            send_command(2, 250, 2000, 2)

    def serial_reset_position(self):
        "Send command to the elevator motor to reset position."

        with open("send.txt", "w") as f:
            f.write("elevator down")
        
        send_command(2, 250, 5000, 2)
    
    def return_position(self):
        "Return the position of the elevator."
        return self.pos

    def print_boxes(self):
        "Print the box in the elevator."
        if self.box == None:
            print("Elevator is empty")
        else:
            self.box.print_box()
    
    def add_box(self, box):
        "Add a box to the elevator."
        box.set_location(1)
        self.box = box
    
    def remove_box(self):
        "Remove a box from the elevator."
        box = self.box
        self.box = None
        return box
    
