from classes.pusher import Pusher
from serial import SerialException
import pytest
def test_pusher():
    e = Pusher()
    with pytest.raises(SerialException):
        e.serial_command_pull()
    with pytest.raises(SerialException):
        e.serial_command_push()            