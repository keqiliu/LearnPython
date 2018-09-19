# Zed Shaw's game source code

from sys import exit
from random import randint
from textwrap import dedent
"""
dedent(text)
    Remove any common leading whitespace from every line in `text`.
"""


# very similar to C# abstract class
class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)  # to mark that no one should instantiate this class


class Death(Scene):
    quips = [
        "You died.",
        "You kinda suck at this.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        # Death.quips vs. self.quips???
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            This is central corridor.
            Entering...
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Central corridor - shoot!
                He eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                Central corridor - dodge!
                Oops.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                Lucky you. 
                Jump to the armory door.
                """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                Enter 2 digits code:
                """))

        code = f"{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            if guess < code:
                print("Make it larger!")
            else:
                print("Lower it.")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                You got it!
                Entering bridge
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes for too many times.
                """))
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print(dedent("""
            The bridge - entering
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                Does not work
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You run to the escape pod
                """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):
    def enter(self):
        print(dedent("""
            There are 5 pods.
            Which one do you take?
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(f"wrong guess. Right pod is {good_pod}")
            return 'death'
        else:
            print(dedent(f"""
                You jump into pod {guess} and hit the eject button.
                You won!
                """))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)  # dict GET value!!
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


# main play part
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
