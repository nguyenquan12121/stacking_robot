position_mapper = ["Conveyor Belt", "Elevator", "Pusher", "Storage"]

class Box:
    def __init__(self, box_id, location, color):
        self.box_id = box_id
        self.location = location
        self.color = color

    def set_location(self, location):
        self.location = location

    def set_color(self, color):
        self.color = color

    def print_box(self):
        print(f"Box ID: {self.box_id}, Location: {position_mapper[self.location]}, Color: {self.color}")
        
    def get_id(self):
        return self.box_id
