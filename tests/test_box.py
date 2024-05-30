from classes.box import Box


def test_box():
    b = Box(1, None)
    assert(b.get_id() == 1)
    b.set_location("l")
    assert(b.location == "l")
