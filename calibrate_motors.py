from classes.elevator import Elevator
from time import sleep


Elevator = Elevator()

Elevator.serial_reset_position()

sleep(5)

Elevator.serial_command_up_3()
    
sleep(5)

Elevator.serial_command_down()

sleep(5)

Elevator.serial_command_up_2()

sleep(5)

Elevator.serial_command_down()

sleep(5)

Elevator.serial_command_up_1()

sleep(5)