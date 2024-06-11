import serial
from classes.pusher import Pusher
from serial import SerialException
import pytest

def ttyACM0_accessibility():
    try:
        # Try to open the interface with a timeout of 1 second
        ser = serial.Serial('/dev/ttyACM0', timeout=1)
        ser.close()
        return True
    except serial.SerialException as e:
        return False


def test_pusher():
    e = Pusher()
    if not ttyACM0_accessibility():
        with pytest.raises(SerialException):
            e.serial_command_pull()
        with pytest.raises(SerialException):
            e.serial_command_push()
    else:          
        e.serial_command_pull()
        e.serial_command_push()
