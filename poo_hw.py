# Write a Python class named Rectangle constructed by 
# a length and width and a method 
# which will compute the area of a rectangle.

class Rectangle:
    def __init__(self,length,width) :
        self.length = length
        self.width = width
    # computes the area of the rectangle
    # reminder rectangle area A = width * length
    def area(self):
        return self.length * self.width

#Create a Vehicle class with
#  max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,max_speed,mileage) :
        self.max_speed = max_speed
        self.mileage = mileage

#Create a Vehicle class without any variables and methods.
class Vehicle:
    def __init__(self) -> None:
        pass

#Create a child class Bus 
# that will inherit all of the variables and methods 
# of the Vehicle class
class Bus(Vehicle):
    def __init__(self) -> None:
        super().__init__()