class BoxQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, box):
        self.queue.append(box)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def print_boxes(self):
        for box in self.queue:
            print(box.print_box())

