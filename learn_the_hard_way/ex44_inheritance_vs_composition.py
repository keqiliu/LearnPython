"""
Most of the uses of inheritance can be simplified or replaced with
composition!!!
"""


class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()  # super is most likely used in __init__

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, Before PARENT altered()")
        super(Child, self).altered()
        print("CHILD, After PARENT altered()")


dad = Parent()
son = Child("Aiya")

dad.implicit()
son.implicit()  # implicit inheritance

dad.override()
son.override()  # override explicitly

dad.altered()
son.altered()  # call super class func


# NOT using inheritance
class Other(object):
    def implicit(self):
        print("OTHER implicit()")

    def override(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER altered()")


class ChildNotInheriting(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        self.other.override()

    def altered(self):
        print("CHILD, Before OTHER altered()")
        self.other.altered()
        print("CHILD, After OTHER altered()")


son_no_inherit = ChildNotInheriting()

son_no_inherit.implicit()
son_no_inherit.override()
son_no_inherit.altered()
