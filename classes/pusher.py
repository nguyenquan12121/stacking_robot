from serial_motor import send_command

class Pusher:
    def __init__(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value
        self.box = None

    def serial_command(self):
        send_command(self.motor_value, self.speed, self.duration, self.direction)
        
    def print_boxes(self):
        if self.box == None:
            print("Pusher is empty")
        else:
            self.box.print_box()

    def add_box(self, box):
        box.set_location(2)
        self.box = box
        self.direction = 1

    def remove_box(self):
        box = self.box
        self.box = None
        return box
    
    def set_values(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value
