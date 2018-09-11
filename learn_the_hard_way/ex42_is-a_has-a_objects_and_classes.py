"""
To-do list:
1. what is "object" class? --> From Study Drill #1
2. Read about "multi inheritance", then try to avoid!!
3. Read about "super", pros & cons
"""

# Animal is-a object
class Animal(object):  # put (object) here! explicit is better than implicit!!
    pass


# Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        # has-a
        self.name = name


# is-a
class Cat(Animal):
    def __init__(self, name):
        # has-a
        self.name = name


# is-a
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

    def get_a_pet(self, pet):
        self.pet = pet


# is-a
class Employee(Person):
    def __init__(self, name, salary):
        # use upper level's init
        super(Employee, self).__init__(name)
        self.pet = "puppy"  # test which to take
        self.salary = salary


# is-a
class Fish(object):
    pass


# is-a
class Salmon(Fish):
    pass


# is-a
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")
katie = Cat("Katie")
mary = Person("Mary")
print("Mary's pet: ", mary.pet)
mary.get_a_pet("Peppa pig")
print("Mary's pet: ", mary.pet)

frank = Employee("Frank", 12000)
print(f"{frank.name}'s pet: {frank.pet}")
frank.get_a_pet("Peppa George")  # can call functions in Super Class
print(f"{frank.name}'s pet: {frank.pet}")

flipper = Fish()
crouse = Salmon()
harry = Halibut()
