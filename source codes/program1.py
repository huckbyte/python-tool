from abc import ABC, abstractmethod


class Animal():
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species
class carnivore:
    def animal_sound(self,animals: list):
        for animal in animals:
            if animal.species == 'cat':
                print('meow')
            elif animal.species == 'dog':
                print('woof-woof')

    @abstractmethod
    def make_sound(self):
        print("pass")

