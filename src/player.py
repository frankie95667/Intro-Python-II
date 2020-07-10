# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name,  current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)
        item.on_take()
        return self.inventory

    def removeItem(self, name):
        try:
            found_item = next(iter([item for item in self.inventory if item.name == name]))
        except:
            print(f"{name} is not in inventory")
            return None
        if(found_item):
            self.inventory.remove(found_item)
            found_item.on_drop()
        else:
            print(f"{name} is not in your inventory")
        return found_item
    
    def getInventory(self):
        print("Inventory")
        print("="*60)
        for i in self.inventory:
            print(f"{i.name} - {i.description}")

    def isInstance(self):
        room_items = [item for item in self.current_room.items if item.__class__.__name__ == "LightSource"]
        player_items = [item for item in self.inventory if item.__class__.__name__ == "LightSource"]
        for i in self.inventory:
            print(i.__class__.__name__)
        if(self.current_room.is_light or len(room_items) or len(player_items)):
            return True
        return False
