class Shelf:
    "Shelf object which keeps track of all the boxes"

    def __init__(self):
        self.floors = [0, 0, 0]
        
    def add_box(self, floor):
        "Add a box to the shelf."
        self.floors[floor - 1] += 1

    def next_floor(self):
        "Return the floor with the least number of boxes."
        min_index = self.floors.index(min(self.floors))
        return min_index + 1

