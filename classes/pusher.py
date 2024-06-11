from serial_motor import send_command

class Pusher:
    "A class for creating a pusher object."
    def __init__(self):
        self.box = None

    def serial_command_push(self):
        "Send command to the pusher motor to push."

        with open("send.txt", "w") as f:
            f.write("pusher out")

        send_command(1, 100, 4000, 2)

    def serial_command_pull(self):
        "Send command to the pusher motor to retract."

        with open("send.txt", "w") as f:
            f.write("pusher in")
        send_command(1, 190, 4000, 1)
