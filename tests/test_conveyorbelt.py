from classes.ConveyorBelt import ConveyorBelt
from classes.box import Box

class TestConveyorBelt: 

    def test_conveyorbelt_box(self):
        cb = ConveyorBelt()
        cb.add_box(Box(1, "l"))
        assert(cb.boxes.size() == 1)
        cb.remove_box()
        assert(cb.boxes.size() == 0)
