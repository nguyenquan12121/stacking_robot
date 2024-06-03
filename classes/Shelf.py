class Shelf:
    def __init__(self):
        self.floors = {1: [], 2:[], 3:[]}
        
    def add_box(self, floor, box):
        if floor <= 3 and floor >= 1:
            box.set_location(3)
            self.floors[floor].append(box)
        else:
            raise("Invalid floor number")
        
    def remove_box(self, floor, box):
        if floor in self.floors and box in self.floors[floor]:
            self.floors[floor].remove(box)
        else:
            raise("Invalid floor number")     
        
    def size(self):
        size = 0 
        for i in range(1,4):
            size += len(self.floors[i])
        return size
    
    def print_boxes(self):
        for floor, boxes in self.floors.items():
            print("Floor {floor}: {boxes}\n")
        