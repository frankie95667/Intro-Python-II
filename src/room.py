# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return (f"""\n{'='*60}\nCurrent Location: {self.name}\n\n{textwrap.fill(self.description, width=60)}\n{'='*60}\n""")

