# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.monsters = []

    def __str__(self):
        items = "\n".join([item.name for item in self.items])
        monsters = "\n".join(self.printMonsters())
        return (
            f"""

{'='*60}
Current Location: {self.name}

{textwrap.fill(self.description, width=60)}

Items
------
{items}

Monsters
------
{monsters}
{'='*60}
""")

    def addItem(self, item):
        self.items.append(item)
        return self.items

    def removeItem(self, name):
        try:
            found_item = next(
                iter([item for item in self.items if item.name == name]))
        except:
            print(f"{name} is not in room")
            return None
        if(found_item):
            self.items.remove(found_item)
        else:
            print(f"{name} is not in the room")
        return found_item

    def addMonster(self, monster):
        self.monsters.append(monster)
        return self.monsters

    def removeMonster(self, name):
        try:
            found_monster = next(
                iter([monster for monster in self.monsters if monster.name == name]))
        except:
            print(f"{name} is not in the room")
            return None
        if(found_monster):
            self.monsters.remove(found_monster)
        return self.monsters

    def getMonster(self, name):
        try:
            found_monster = next(
                iter([monster for monster in self.monsters if monster.name == name]))
        except:
            print(f"{name} is not in the room")
            return None
        return found_monster

    def printMonsters(self):
        return [str(monster) for monster in self.monsters]
