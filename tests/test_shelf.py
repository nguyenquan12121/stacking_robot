from serial import SerialException
from classes.Shelf import Shelf

def test_shelf():
    s = Shelf()
    s.add_box(1)
    assert(s.floors[0] == 1)
    assert(s.next_floor() == 2)
