class Shelf:
    def __init__(self):
        self.floors = {"red": [], "green":[], "blue":[]}
        
    def add_box(self, box):
        floor = box.color
        if floor in self.floors:
            box.set_location(3)
            self.floors[floor].append(box)
        else:
            raise("Invalid color")
        
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
