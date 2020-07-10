
class Item:
    def __init__(self, name, description):
        self.name = name.split(" ")[0]
        self.description = description

    def __str__(self):
        return f"Name: {self.name}"

    def on_take(self):
        print(f"You have picked up {self.name}")
    
    def on_drop(self):
        print(f"You have dropped {self.name}")