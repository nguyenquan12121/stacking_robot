from classes.elevator import Elevator
from classes.box import Box

class TestElevator:
    def test_elevator(self):
        e = Elevator()
        b = Box(1, "l")
        e.add_box(b)
        assert(e.return_position() == 0)
        assert(e.box == b)    
        assert(e.remove_box() == b)
