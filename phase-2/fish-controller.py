from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price


class Ornament(Base):
    comfort = 1
    price = 5

    def __init__(self):
        super().__init__(self.comfort, self.price)


class Plant(Base):
    comfort = 5
    price = 10

    def __init__(self):
        super().__init__(self.comfort, self.price)


class BaseFish(ABC):
    increase_size = 5

    @abstractmethod
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value == "":
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += self.increase_size


class FreshwaterFish(BaseFish):
    size = 3
    increase_size = 3
    water = "Fresh"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.size, price)
        
class SaltwaterFish(BaseFish):
    size = 5
    increase_size = 3
    water = "Salty"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.size, price)


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if not self.fish:
            names = 'none'
        else:
            names = " ".join([fish.name for fish in self.fish])
        return f"{self.name}:\n" \
               f'Fish: {names}\n' \
               f'Decorations: {len(self.decorations)}\n' \
               f'Comfort: {self.calculate_comfort()}\n'

    # def __str__(self):
    #     return f"{self.name}:\n" \
    #            f"Fish: {' '.join((fish.name for fish in self.fish) if self.fish else 'none')}\n" \
    #            f"Decorations: {len(self.decorations)}\n" \
    #            f"Comfort: {self.calculate_comfort()}"


class FreshwaterAquarium(BaseAquarium):
    capacity = 50
    water = "Fresh"

    def __init__(self, name):
        super().__init__(name, self.capacity)

class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def get_fish(fish_type, fish_name, fish_species, price):
        fish = None
        if fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)
        return fish

    def get_aquarium(self, aquarium_name):
        try:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        except IndexError:
            aquarium = None
        return aquarium

    def add_aquarium(self, aquarium_type, aquarium_name):
        valid_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."
        if aquarium_type == valid_aquariums[0]:
            aquarium = FreshwaterAquarium(aquarium_name)
        else:
            aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        valid_decorations = ["Ornament", "Plant"]
        if decoration_type not in valid_decorations:
            return "Invalid decoration type."
        if decoration_type == valid_decorations[0]:
            decoration = Ornament()
        else:
            decoration = Plant()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.get_aquarium(aquarium_name)
        if aquarium is not None and not decoration == "None":
            aquarium.add_decoration(decoration)
            if self.decorations_repository.remove(decoration):
                return f"Successfully added {decoration_type} to {aquarium_name}."
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        valid_fish = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish:
            return f"There isn't a fish of type {fish_type}."
        fish = self.get_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.get_aquarium(aquarium_name)
        if not aquarium.water == fish.water:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.get_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.get_aquarium(aquarium_name)
        fish_price = sum(fish.price for fish in aquarium.fish)
        decorations_price = sum(decoration.price for decoration in aquarium.decorations)
        total_price = fish_price+decorations_price
        return f"The value of Aquarium {aquarium_name} is {total_price:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += aquarium.__str__()
        return result
