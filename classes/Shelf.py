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

        
    def remove_box(self, floor, box):
        "Remove a box from the shelf."
        
        if floor in self.floors and box in self.floors[floor]:
            self.floors[floor].remove(box)
        else:
            raise("Invalid floor number")     
    
    def print_boxes(self):
        "Print the boxes on the shelf."

        for i, color in enumerate(self.floors):
            print("FLOOR " + str(i) + " colored " + color)
            for box in self.floors[color]:
                box.print_box()
