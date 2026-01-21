class ClassTest:
    def instance_method(self):
        print(f"Called instance of {self}")

test = ClassTest()
test.instance_method()
# or 
ClassTest.instance_method(test)

# above example shows the instance method of class i.e it requires instance test to run that class

class ClassTest2:
    def instance_method(self):
        print(f"Called instance of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("called static_method")

# since is a class method no longer requires the instance
# a method that uses the class for something then decorate using @classmethod
ClassTest2.class_method()       # no longer need to pass object 

# Not really a method. just a function placed inside a class. doesn't have any info about the class or the object
# a method that doesn't use class or instance you can decorate it with @staticmethod
ClassTest2.static_method()

# usecase: 
# instance method: are used for mostthings, when action uses the data inside the object : use instance method
#                   method to modify some sort of data inside self or obj then use instance method

# class method: often used as factories

# staticmethod: to place an method inside a class: makes sense logically or feels as it belongs there


# mostly used are class and instance method 

# Classmethod eg as a factory:

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"
    
    @classmethod
    def hardcover(cls, name, page_weight):         # since is a class method takes class i.e cls as first parameter
        return Book(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def hardcover(cls, name, page_weight):        # since Book and cls both are equivalent to class they are interchangable
        return cls(name, cls.TYPES[1], page_weight )        
    
# using class inside a method defined inside a class: 
# to create a new object inside a class

book = Book("harry potter", "comic book", 1500)         # since now we have a class method no longer need to create your own object first
print(book)

book2 = Book.hardcover("Harry potter", 1500)
print(book2)

book3 = Book.hardcover("Harry potter", 1500)
print(book3)

# good practice is to use cls insted of Book i.e class name because it provides little more flexibility