from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_name, weight, age, gender):
        self.animal_name = animal_name
        self.weight = weight
        self.food_eaten = 0
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, animal_name, weight, wing_size):
        super().__init__(animal_name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__animal_name__} [{self.animal_name}, " \
               f"{self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, animal_name, weight, living_region):
        super().__init__(animal_name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__animal_name__} [{self.animal_name}, " \
               f"{self.weight}, {self.living_region}, {self.food_eaten}]"


from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Owl(Bird):
    WEIGHT_COEFFICIENT = 0.25

    def __init__(self, animal_name, weight, wing_size):
        super().__init__(animal_name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__animal_name__} does not eat {food.__class__.__animal_name__}!"
        self.weight += Owl.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_COEFFICIENT = 0.35

    def __init__(self, animal_name, weight, wing_size):
        super().__init__(animal_name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.weight += Hen.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Mouse(Mammal):
    WEIGHT_COEFFICIENT = 0.10

    def __init__(self, animal_name, weight, living_region):
        super().__init__(animal_name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, (Fruit, Vegetable)):
            return f"{self.__class__.__animal_name__} does not eat {food.__class__.__animal_name__}!"
        self.weight += Mouse.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_COEFFICIENT = 0.40

    def __init__(self, animal_name, weight, living_region):
        super().__init__(animal_name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__animal_name__} does not eat {food.__class__.__animal_name__}!"
        self.weight += Dog.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_COEFFICIENT = 0.30

    def __init__(self, animal_name, weight, living_region):
        super().__init__(animal_name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if not isinstance(food, (Meat, Vegetable)):
            return f"{self.__class__.__animal_name__} does not eat {food.__class__.__animal_name__}!"
        self.weight += Cat.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity

class Kitten(Cat):
    def __init__(self, animal_name, age, gender="Female"):
        super().__init__(animal_name, age, gender)

    @staticmethod
    def make_sound():
        return "Meow"

    def __repr__(self):
        return f"This is {self.animal_name}. {self.animal_name} " \
               f"is a {self.age} year old {self.gender} " \
               f"{self.__class__.__name__}"

class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Hiss"

    def __repr__(self):
        return f"This is {self.name}. {self.name} " \
               f"is a {self.age} year old {self.gender} " \
               f"{self.__class__.__name__}"


class Tiger(Mammal):
    WEIGHT_COEFFICIENT = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Tiger.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity
