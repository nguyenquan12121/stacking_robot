import pytest
from serial import SerialException
from classes.elevator import Elevator
from classes.box import Box

def test_elevator():
    e = Elevator()
    b = Box(1, "l")
    e.add_box(b)
    assert(e.return_position() == 0)
    assert(e.box == b)    
    assert(e.remove_box() == b)
    
def test_elevator_serial():
    e = Elevator()
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
