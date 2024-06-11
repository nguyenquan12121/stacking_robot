import pytest
import serial
from serial import SerialException
from classes.elevator import Elevator
from classes.box import Box

def ttyACM0_accessibility():
    try:
        # Try to open the interface with a timeout of 1 second
        ser = serial.Serial('/dev/ttyACM0', timeout=1)
        ser.close()
        return True
    except serial.SerialException as e:
        return False


def test_elevator():
    e = Elevator()
    b = Box(1, "l")
    e.add_box(b)
    assert(e.return_position() == 0)
    assert(e.box == b)    
    assert(e.remove_box() == b)
    
def test_elevator_serial():
    e = Elevator()
    if not ttyACM0_accessibility():
        with pytest.raises(SerialException):
            e.serial_command_up_1()
        with pytest.raises(SerialException):
            e.serial_command_up_2()
        with pytest.raises(SerialException):
            e.serial_command_up_3()
        with pytest.raises(SerialException):
            e.pos = 1
            e.serial_command_down()
        with pytest.raises(SerialException):
            e.pos = 2
            e.serial_command_down()
        with pytest.raises(SerialException):
            e.pos = 3
            e.serial_command_down()                
        with pytest.raises(SerialException):
            e.serial_reset_position()
    else:
        e.serial_command_up_1()
        e.serial_command_up_2()
        e.serial_command_up_3()
        e.pos = 1
        e.serial_command_down()
        e.pos = 2
        e.serial_command_down()         
        e.pos = 3
        e.serial_command_down()                 
        e.serial_reset_position()

# Test for print output
def test_print_boxes_empty(capfd):
    elevator = Elevator()
    elevator.print_boxes()

    # Capture the output
    captured = capfd.readouterr()
    assert captured.out.strip() == "Elevator is empty"
    
# Test for print output
def test_print_boxes_empty(capfd):
    elevator = Elevator()
    b = Box(1,1)
    elevator.add_box(b)
    elevator.print_boxes()

    # Capture the output
    captured = capfd.readouterr()
    assert captured.out.strip() == "Box ID: 1, Location: 2, Color: None"    
