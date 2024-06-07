class Shelf:
    def __init__(self):
        self.floors = [0, 0, 0]
        
    def add_box(self, floor):
        self.floors[floor] += 1

    def next_floor(self):
        min_index = self.floors.index(min(self.floors))
        return min_index + 1

        
    def remove_box(self, floor, box):
        if floor in self.floors and box in self.floors[floor]:
            self.floors[floor].remove(box)
        else:
            raise("Invalid floor number")     
        
#    def size(self):
#        size = 0 
#        for i in range(1,4):
#            size += len(self.floors[i])
#        return size
    
    def print_boxes(self):
        for i, color in enumerate(self.floors):
            print("FLOOR " + str(i) + " colored " + color)
            for box in self.floors[color]:
                box.print_box()
