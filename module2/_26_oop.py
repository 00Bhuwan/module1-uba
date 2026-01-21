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

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"      # !r puts quote around name making it cleaner
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")

printer = Device("printer", "USB")
print(printer)
printer.disconnect()

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()  # search disconnect in Printer -> then Device class -> then Object class
printer.print(30)