from serial import send_command

class Elvator:
    def __init__(self, speed, duration, motor_value, boxes):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value

    def serial_command(self):
        send_command(self.motor_value, self.speed, self.duration)
    
    def print_boxes(self):
        for box in self.boxes:
            print(box)