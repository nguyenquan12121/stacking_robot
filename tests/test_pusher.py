from classes.pusher import Pusher
from classes.box import Box
class TestPusher:
    def test_pusher(self):
        e = Pusher(1,1,1)
        b = Box(1, "l")
        e.add_box(b)
        assert(e.box == b)
        assert(e.remove_box() == b)