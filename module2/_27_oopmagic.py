class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self):
    #     return f"Person {self.name}, Age {self.age}"
    
    def __repr__(self):
        return f"{self.name} is of age {self.age}"
    
bob = Person("Bon", 34)
print(bob)

# str magic method: used when you ask it to print an object in its string representation

# if both str and repr method used in single class only str is called
# repr is used in python debugger 


# both are used to represent and object in string format: do use one if necessary not both at the same time.

# usecase:
# repr used representation of class that allows use of data included inside to create to recreate the class object if we want to.
# str used to print the class object for users to read