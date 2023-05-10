class BankAccount:
    rate_of_interest = 5
    min_balance = 100
    min_balance_fees = 10
    bank_name = 'ABC bank, XYZ Street, New Delhi'
    def __init__(self, name, balance=0, bank=bank_name):
        self.name = name
        self.balance = balance
        self.bank = bank
    def display(self):
        print(self.name, self.balance, self.bank)
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
a1 = BankAccount('Mike', 200, 'PQR Bank Delhi')
a2 = BankAccount('Tom')
a1.display()
a2.display()

""" product"""

class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
    @property
    def selling_price(self):
        return self.marked_price - 0.01 * self.discount * self.marked_price
    def display(self):
        print(self.id,  self.marked_price,  self.discount)
    @property
    def value(self):
        return self._x
    @value.setter
    def value(self, val):
        self._x = val
    @value.deleter
    def value(self):
        print('value deleted')
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        self._y = val

p1 = Product('A234', 100, 5)
p2 = Product('X879', 400, 6)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

print(p1.id, p1.selling_price)
print(p2.id, p2.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)

class Product1:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    def display(self):
        print(self._x, self._y)
    @property
    def value(self):
        return self._x
    @value.setter
    def value(self, val):
        self._x = val
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, val):
        self._y = val


""" stacks  """

class Stack:
    MAX_SIZE = 5
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, item):
        if self.size() == Stack.MAX_SIZE:
            raise RuntimeError('Stack is full')
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()
    def display(self):
        print(self.items)

st = Stack()

print("1.Push")
print("2.Pop")
print("3.Peek")
print("4.Size")
print("5.Display")
print("6.Quit")
