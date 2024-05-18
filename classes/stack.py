class Stack:
    def __init__(self):
        self.stack = []

    def add_box(self, box):
        box.set_location(3)
        self.stack.append(box)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    def print_boxes(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for item in self.stack:
                item.print_box()