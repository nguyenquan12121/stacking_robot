from serial_motor import send_command

class Pusher:
    def __init__(self):
        self.box = None

    def serial_command_push(self):
        with open("send.txt", "w") as f:
            f.write("pusher out")

        send_command(1, 200, 1000, 2)

    def serial_command_pull(self):
        with open("send.txt", "w") as f:
            f.write("pusher in")
        send_command(1, 200, 1000, 1)
        
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
