from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')
            

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__(species=None)
        self.sound = "Meow"

    def make_sound(self):
        return self.sound


class Dog(Animal):
    def __init__(self):
        super().__init__(species=None)
        self.sound = "Woof-woof"

    def make_sound(self):
        return self.sound


animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())
