""" class person intoduction """
class Person:
    species  = 'Homo sapiens'
    count = 0
    def __init__(self,id):
        self.id = id
    @classmethod
    def show_count(cls):
        print(f'There are {cls.count} {cls.species}')
    @staticmethod
    def detais():
        pass
class Teacher(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'T'
class Student(Person):
    def __init__(self,id):
        super().__init__(id)
        self.id += 'S'
class TeachingAssistant(Student, Teacher):
     def __init__(self,id):
        super().__init__(id)
"""class person instances  """

x = TeachingAssistant('2675')
print(x.id)
y = Student('4567')
print(y.id)
z = Teacher('3421')
print(z.id)
p = Person('5749')
print(p.id)

"""class book  """

class Book:
    def __init__(self,isbn, title,author,publisher,pages,price,copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
    def display(self):
        print(self.title)
        print(f'ISBN : {self.isbn}')
        print(f'Price : {self.price}')
        print(f'Number of copies : {self.copies}')
        print('.' * 50)
    @staticmethod
    def detais():
        pass
    def in_stock(self):
        return True if self.copies>0 else False
    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print('The book is out of stock')

"""class book instances """

book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.display()
book2.display()
book3.display()
book4.display()

book3.sell()
book3.sell()
book3.sell()
book3.sell()
book3.sell()
book3.sell()

"""  course class   """

class Course:
    def __init__(self, title, instructor, lectures, price):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0
    def __str__(self):
        return f'{self.title} by {self.instructor}'
    @staticmethod
    def detais():
        pass
    def new_user_enrolled(self, user):
        self.users.append(user)
    def received_a_rating(self, new_rating):
        self.avg_rating = (self.avg_rating * self.ratings + new_rating)/(self.ratings + 1)
        self.ratings += 1 
    def show_details(self):
        print('Course Title : ', self.title)
        print('Intructor : ', self.instructor)
        print('Price : ', self.price)
        print('Number of Lectures : ', self.lectures)
        print('Users : ', self.users)
        print('Average rating : ', self.avg_rating)
class VideoCourse(Course):
    def __init__(self,title,instructor,lectures,price,length_video):
        super().__init__(title,instructor,lectures,price)
        self.length_video = length_video
    def show_details(self):
        super().show_details()
        print('Video Length : ',  self.length_video)
class PdfCourse(Course):
    def __init__(self,title,instructor,lectures,price,pages):
        super().__init__(title,instructor,lectures,price)
        self.pages = pages
    def show_details(self):
        super().show_details()
        print('Number of pages : ',  self.pages)

"""class course instances """

vc = VideoCourse('Learn C++', 'Jack', 30, 50, 10)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Max')
vc.new_user_enrolled('Tom')
vc.received_a_rating(3)
vc.received_a_rating(5)
vc.received_a_rating(4)
vc.show_details()
print()
pc = PdfCourse('Learn Java', 'Jim', 35, 50, 1000)
pc.new_user_enrolled('Allen')
pc.new_user_enrolled('Mary')
pc.new_user_enrolled('JIm')
pc.received_a_rating(5)
pc.received_a_rating(4)
pc.received_a_rating(4.5)
pc.show_details()



