class HotPizza:
    def __init__(self, Pizza_name, Pizza_Price, Ingrent):
        self.Pizza_name = Pizza_name
        self.Pizza_Price = Pizza_Price
        self.Ingrent = dict(Ingrent)
        self.Pizza_Order = False

    def Extra_Pizza_Order(self, Ingrent, quantity, Ingrent_Pizza_Price):
        if self.Pizza_Order:
            return f"Pizza {self.Pizza_name} already prepared !"
        
        if Ingrent not in self.Ingrent:
            self.Ingrent[Ingrent] = quantity
            self.Pizza_Price += quantity * Ingrent_Pizza_Price
            
        else:
            self.Ingrent.update({Ingrent: self.Ingrent[Ingrent]+quantity})
            self.Pizza_Price += quantity * Ingrent_Pizza_Price

    def Digant_ingre(self, Ingrent, quantity, Ingrent_Pizza_Price):
        if self.Pizza_Order:
            return f"Pizza {self.Pizza_name} already prepared !"
        
        if Ingrent in self.Ingrent:
            
            if self.Ingrent[Ingrent] >= quantity:
                self.Ingrent.update({Ingrent: self.Ingrent[Ingrent]-quantity})
                self.Pizza_Price -= quantity * Ingrent_Pizza_Price
                return
            
            return f"Please check again the desired quantity of {Ingrent}!"
        
        return f"Wrong Ingrent selected! We do not use {Ingrent} in {self.Pizza_name}!"

    def Pizza_Order_Request(self):
        
        self.Pizza_Order = True
        
        return f"You've Pizza_Order pizza {self.Pizza_name} prepared with " \
               f"{', '.join((': '.join((str(i), str(q)))) for i, q in self.Ingrent.items())} " \
               f"and the Pizza_Price will be {self.Pizza_Price}lv."


Hezron = HotPizza('Hezron', 44, {'Chill&Cheese': 2, 'Cheese': 4})
Hezron.Extra_Pizza_Order('mozzarella', 4, 3.5)
Hezron.Extra_Pizza_Order('Chill&Cheese', 4, 4)
Hezron.Digant_ingre('Chill&Cheese', 4, 4)
print()
print(Hezron.Digant_ingre('bacon', 4, 1.5))
print(Hezron.Digant_ingre('Cheese', 2, 3.5))
Hezron.Digant_ingre('Chill&Cheese', 2, 4)
print(Hezron.Pizza_Order_Request())
print(Hezron.Extra_Pizza_Order('Chill&Cheese', 4, 4))
