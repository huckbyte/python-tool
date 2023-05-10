class MAMMAL:
    def __init__(self, Animal_name, Animal_Type, Animal_Sound):
        self.Animal_name = Animal_name
        self.type = Animal_Type
        self.Animal_Sound = Animal_Sound
        self.Animal_Kingdom = "animals"

    def Sound(self):
        return f"{self.Animal_name} makes {self.Animal_Sound}"

    def kingdom(self):
        return self.Animal_Kingdom

    def Animal_type(self):
        return f"{self.Animal_name} is of type {self.type}"

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, Animal_name, Animal_age, Animal_gender):
        self.Animal_name = Animal_name
        self.Animal_age = Animal_age
        self.Animal_gender = Animal_gender

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class Cat(Animal):
    def __init__(self, Animal_name, Animal_age, Animal_gender):
        super().__init__(Animal_name, Animal_age, Animal_gender)

    @staticmethod
    def sound():
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.Animal_name}. {self.Animal_name} " \
               f"is a {self.Animal_age} year old {self.Animal_gender} " \
               f"{self.__class__.__name__}"

class Dog(Animal):
    def __init__(self, Animal_name, Animal_age, Animal_gender):
        super().__init__(Animal_name, Animal_age, Animal_gender)

    @staticmethod
    def sound():
        return "Woof!"

    def __repr__(self):
        return f"This is {self.Animal_name}. {self.Animal_name} " \
               f"is a {self.Animal_age} year old {self.Animal_gender} " \
               f"{self.__class__.__name__}"

class Tomcat(Cat):
    def __init__(self, Animal_name, Animal_age, Animal_gender="Male"):
        super().__init__(Animal_name, Animal_age, Animal_gender)

    @staticmethod
    def sound():
        return "Hissssss"

    def __repr__(self):
        return f"This is {self.Animal_name}. {self.Animal_name} " \
               f"is a {self.Animal_age} year old {self.Animal_gender} " \
               f"{self.__class__.__name__}"

class Kitten(Cat):
    def __init__(self, Animal_name, Animal_age, Animal_gender="Female"):
        super().__init__(Animal_name, Animal_age, Animal_gender)

    @staticmethod
    def sound():
        return "Meow"

    def __repr__(self):
        return f"This is {self.Animal_name}. {self.Animal_name} " \
               f"is a {self.Animal_age} year old {self.Animal_gender} " \
               f"{self.__class__.__name__}"
