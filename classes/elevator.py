from serial import send_command

class Elevator:
    def __init__(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value
        self.box = None
        self.direction = 1

    def serial_command(self):
        send_command(self.motor_value, self.speed, self.duration, self.direction)
    
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
    
    def set_values(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value
        
