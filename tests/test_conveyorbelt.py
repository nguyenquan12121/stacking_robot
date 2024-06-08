import pytest
from serial import SerialException
from classes.ConveyorBelt import ConveyorBelt
from classes.box import Box

def test_conveyorbelt_box():
    cb = ConveyorBelt()
    cb.add_box(Box(1, "l"))
    assert(cb.boxes.size() == 1)
    cb.remove_box()
    assert(cb.boxes.size() == 0)
    
def test_conveyor_serial():
    cb = ConveyorBelt()
    with pytest.raises(SerialException):
        cb.serial_command()