# Created by Youssef Elashry to allow two-way communication between Python3 and Unity to send and receive strings

# Feel free to use this in your individual or commercial projects BUT make sure to reference me as: Two-way communication between Python 3 and Unity (C#) - Y. T. Elashry
# It would be appreciated if you send me how you have used this in your projects (e.g. Machine Learning) at youssef.elashry@gmail.com

# Use at your own risk
# Use under the Apache License 2.0

# Example of a Python UDP server

class Communicate():
    "Class for sending data to the Unity application."

    def __init__(self):
        import UdpComms as U
        import time

        # Create UDP socket to use for sending (and receiving)
        self.sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=False, suppressWarnings=True)


        self.sock.SendData('Action: connected to the python') # Send this string to other application

        time.sleep(1)

        self.sock.SendData('Action: None') # Send this string to other application



    def send_data(self, action):
        if action != None:
            self.sock.SendData('Action: ' + action) # Send this string to unity application
