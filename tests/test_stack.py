import pytest

from classes.stack import Stack
from classes.box import Box

class TestStack:
    def test_stack(self):
        e = Stack()
        e.add_box(Box(1, "l"))
        assert(e.size() == 1)
        e.pop()
        assert(e.size() == 0)
    def test_stack_exception(self):
        e = Stack()
        with pytest.raises(IndexError, match="Stack is empty"):
            e.pop()
        
    