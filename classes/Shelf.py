class Shelf:
    "Shelf object which keeps track of all the boxes"

    def __init__(self):
        self.floors = [0, 0, 0]
        self.maxval = 2
        
    def add_box(self, floor):
        "Add a box to the shelf."
        self.floors[floor - 1] += 1

    def next_floor(self):
        "Return the floor with the least number of boxes."
        min_index = self.floors.index(min(self.floors))
        return min_index + 1
    
    def isFull(self):
        if (self.floors[0] == self.maxval and self.floors[1] == self.maxval and self.floors[2] == self.maxval):
            return True
        return False

