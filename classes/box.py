position_mapper = ["Conveyor Belt", "Elevator", "Pusher", "Storage"]

class Box:
    def __init__(self, box_id, position):
        self.box_id = box_id
        self.position = position

    def set_position(self, position):
        self.position = position

    def print_box(self):
        print(f"Box ID: {self.box_id}, Position: {position_mapper[self.position]}")
        
    def get_id(self):
        return self.box_id