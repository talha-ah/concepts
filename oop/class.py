class Pet:
    total_pets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.total_pets += 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    @classmethod
    def get_total_pets(cls):
        return f"Number of total pets: {cls.total_pets}"

    @staticmethod
    def speak():
        return 'I don"t know what to speak'

    # method overloading - parameters differs
    def move_tail(self, direction, *args):
        movements = direction

        for i in args:
            movements += ", " + i

        return movements


class Dog(Pet):
    # method overriding - this method is available in the parent class
    def speak(self):
        return "Bark"


# dog = Pet("Dog", 120)
# cat = Pet("Cat", 120)

# print(Pet.get_total_pets())
# print(Pet.speak())

# print(dog.get_total_pets())
# print(dog.speak())

# print(dog.move_tail("right"))
# print(dog.move_tail("right", "left", "up"))


dog = Dog("Dog", 120)
print(dog.speak())
