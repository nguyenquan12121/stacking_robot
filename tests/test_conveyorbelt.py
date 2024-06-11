import serial
import pytest
from serial import SerialException
from classes.ConveyorBelt import ConveyorBelt
from classes.box import Box

def ttyACM0_accessibility():
    try:
        # Try to open the interface with a timeout of 1 second
        ser = serial.Serial('/dev/ttyACM0', timeout=1)
        ser.close()
        return True
    except serial.SerialException as e:
        return False

def test_conveyorbelt_box():
    cb = ConveyorBelt()
    cb.add_box(Box(1, "l"))
    assert(cb.boxes.size() == 1)
    cb.remove_box()
    assert(cb.boxes.size() == 0)
    
def test_conveyor_serial():
    cb = ConveyorBelt()
    if not ttyACM0_accessibility():
        with pytest.raises(SerialException):
            cb.serial_command()
    else:           
        cb.serial_command()
