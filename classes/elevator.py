from serial_motor import send_command
from time import sleep

class Elevator:
    def __init__(self):
        self.box = None
        self.pos = 0

    def serial_command_up_3(self):
        sleep(2)
        send_command(2, 250, 9000, 1)
        sleep(9)
        send_command(2, 250, 3000, 1)
        sleep(8)
        self.pos = 3

    def serial_command_up_2(self):
        sleep(2)
        send_command(2, 250, 6000, 1)
        sleep(8)
        self.pos = 2
    
    def serial_command_up_1(self):
        sleep(2)
        send_command(2, 250, 1500, 1)
        sleep(2)
        self.pos = 1
    
    def serial_command_down(self):
        if (self.pos == 3):
            send_command(2, 250, 5000, 2)
        
        if (self.pos == 2):
            send_command(2, 250, 4000, 2) # TODO: GET VALUES

        if (self.pos == 1):
            send_command(2, 250, 2000, 2) # TODO: GET VALUES

    def serial_reset_position(self):
            send_command(2, 250, 5000, 2) # TODO: GET VALUES
    
    def return_position(self):
        return self.pos

    def print_boxes(self):
        if self.box == None:
            print("Elevator is empty")
        else:
            self.box.print_box()
    
    def add_box(self, box):
        box.set_location(1)
        self.box = box
    
    def remove_box(self):
        box = self.box
        self.box = None
        return box
    
