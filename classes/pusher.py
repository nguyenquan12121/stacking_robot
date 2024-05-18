from serial import send_command

class Pusher:
    def __init__(self, speed, duration, motor_value):
        self.speed = speed
        self.duration = duration
        self.motor_value = motor_value

    def serial_command(self):
        send_command(self.motor_value, self.speed, self.duration)
        