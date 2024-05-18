from serial import send_command

class Pusher:
    def __init__(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value
        self.box = None

    def serial_command(self):
        send_command(self.motor_value, self.speed, self.duration)
        
    def print_boxes(self):
        print(self.box.print_box())

    def add_box(self, box):
        box.set_position(2)
        self.box = box
