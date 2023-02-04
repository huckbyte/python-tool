from abc import ABC, abstractmethod

class Client:
    def __init__(self, nam: str):
        self.nam = nam
        self.prodcts = {}
        
    @property
    def nam(self):
        return self.__nam
    
    @nam.setter
    def nam(self, x):
        if x == "":
            raise ValueError("Provide the Client's name .....")
        self.__nam = x


class Client_List:
    def __init__(self):
        self.Customer = []

    def Add_Customer(self, Client: Client):
        if Client in self.Customer:
            raise ValueError(f"Client {Client.nam} exists.")
        self.Customer.append(Client)

    def Remove_Customer(self, Client_nam: str):
        Client = self.Search_Customer(Client_nam)
        if Client == "None":
            raise ValueError(f"Client {Client_nam} missing.")
        self.Customer.remove(Client)
        return f"Removed Client: {Client_nam}"

    def Search_Customer(self, Client_nam: str):
        try:
            Client = [c for c in self.Customer if c.nam == Client_nam][0]
        except IndexError:
            Client = None
        if Client is None:
            return "None"
        return Client
    
class Iteam(ABC):
    @abstractmethod
    def __init__(self, nam: str, product_quantity: int):
        self.nam = nam
        self.product_quantity = product_quantity

    @property
    def nam(self):
        return self.__nam

    @nam.setter
    def nam(self, x):
        if x == "":
            raise ValueError("Provide the Iteam name ......")
        self.__nam = x

    @property
    def product_quantity(self):
        return self.__product_quantity

    @product_quantity.setter
    def product_quantity(self, y):
        if y <= 0:
            raise ValueError("Provide the product value name .....")
        self.__product_quantity = y
        
class IteamList:
    def __init__(self):
        self.prodcts = []

    def Add_Customer(self, Iteam: Iteam):
        if Iteam in self.prodcts:
            raise ValueError(f"Iteam {Iteam.nam} already exists.")
        self.prodcts.append(Iteam)
        return f"Iteam {Iteam.nam} successfully Added Customerer in the list."

    @staticmethod
    def Reduce(Iteam: Iteam, product_quantity: int):
        Iteam.product_quantity -= product_quantity
        return f"Left product_quantity of {Iteam.nam}: {Iteam.product_quantity}"

    def Search_Customer(self, Iteam_nam: str):
        try:
            Iteam = [p for p in self.prodcts if p.nam == Iteam_nam][0]
        except IndexError:
            Iteam = None
        if Iteam is None:
            return "None"
        return Iteam
    

class Food(Iteam):
    quantity = 15

    def __init__(self, nam):
        super().__init__(nam, self.product_quantity)

class Drink(Iteam):
    quantity = 10

    def __init__(self, nam):
        super().__init__(nam, self.product_quantity)

