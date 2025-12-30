# name of class should always start with Captial letter

class Addition:
    def __init__(self, num1, num2):
        print("This is a constructor space")
        self.num1 = num1             # attribute for a class
        self.__num2 = num2           # self.__num2 indicates it is private doesnt' get inherited in child :see below
    
    def add(self):                  # add() is method for the class
        print("result is ", self.num1 + self.__num2)

    def get_val(self):
        print(f"first variable: {self.num1} and second variable: {self.__num2}")     
        # can access encapsulated private attribute using this method
    
# addition = Addition(12, 34)
# addition.add()

class Substraction(Addition):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)          # inherits from class Addition
        self.num2 = num2
        super().add()

    def sub(self):
        print("result is ", self.num1 - self.num2)

    def get_val(self):
        print(f"first variable: {self.num1} and second variable: {self.num2}")

'''
subtraction = Substraction(32, 12)
subtraction.sub()
subtraction.add()

print(addition.num1) # can access the value
# print(addition.num2)  # cannot access

# Polymorphism: Same name having different funtionality in class
addition.get_val()
subtraction.get_val()

'''