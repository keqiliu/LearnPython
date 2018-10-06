class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
    This is central corridor.
    Entering...
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
    Enter 3 digits code:
""")

the_bridge = Room("The Bridge",
"""
    The bridge - entering
""")

escape_pod = Room("Escape Pod",
"""
    There are 5 pods.
    Which one do you take?
""")

the_end_winner = Room("The End",
"You won! Good job."
)

the_end_loser = Room("The End",
"Oops. You jump into a random pod and escape out of the space."
)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "Ai ya!")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '233': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is security problem here.
    Who gets to set name?
    """
    return globals().get(name)

def name_room(room):
    """
    Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
