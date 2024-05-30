from classes.ConveyorBelt import ConveyorBelt
from classes.box import Box

class TestConveyorBelt:
    def test_conveyorbelt(self):
        cb = ConveyorBelt(1,1,1)
        cb.set_values(1,1,1,1)
        assert(cb.speed == 1)
        assert(cb.duration == 1)
        assert(cb.motor_value == 1)    
        assert(cb.direction == 1)    

    def test_conveyorbelt_box(self):
        cb = ConveyorBelt(1,1,1)
        cb.add_box(Box(1, "l"))
        assert(cb.boxes.size() == 1)
        cb.remove_box()
        assert(cb.boxes.size() == 0)
