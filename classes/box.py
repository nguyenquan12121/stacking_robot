position_mapper = ["1", "2", "3"]

class Box:
    "A class for creating a box object."

    def __init__(self, box_id, location):
        "Initializes the box with a box ID and location."
        self.box_id = box_id
        self.location = location
        self.color = None

    def set_location(self, location):
        "Sets the location of the box."
        self.location = location

    def set_color(self, color):
        "Sets the color of the box."
        self.color = color

    def print_box(self):
        "Prints the box ID, location, and color."
        print(f"Box ID: {self.box_id}, Location: {position_mapper[self.location]}, Color: {self.color}")
        
    def get_id(self):
        "Returns the box ID."
        return self.box_id
