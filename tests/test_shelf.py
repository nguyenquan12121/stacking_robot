from classes.Shelf import Shelf
from classes.box import Box
def test_shelf_add_box():
    s = Shelf()
    b = Box(1,1)
    s.add_box(1,b)
    assert(s.floors[0] == 1)
    assert(s.next_floor() == 2)
    
def test_shelf_next_floor():
    s = Shelf()
    assert(s.next_floor() == 1)

def test_shelf_is_not_full():
    s = Shelf()
    assert s.isFull() == False

def test_shelf_is_full():
    s = Shelf()
    b = Box(1,0)
    for i in range(1,4):
        s.add_box(i,b)
        s.add_box(i,b)
    assert s.isFull() == False
    assert s.floorFull(1) == False