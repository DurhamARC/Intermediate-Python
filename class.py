# define elephant size
elephant_x = 5
elephant_y = 5
elephamt_h = 5

# define refrigerator size
refrigerator_x = 6
refrigerator_y = 6
refrigerator_h = 6


def open_refrigerator_door():
    print('Refrigerator door is opened')

def package_elephant():
    print('Elephant is packaged')

def put_elephant_to_refrigerator():
    print('Elephant is in the fridge already')

def close_refrigerator_door():
    print('Close the refrigerator door')


# compare size
if elephant_x < refrigerator_x and elephant_y < refrigerator_y and elephamt_h < refrigerator_h:
   open_refrigerator_door()
   package_elephant()
   put_elephant_to_refrigerator()
   close_refrigerator_door()
else:
    print('refrigerator is too small to put elephant')

##################

class Elephant:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def package(self):
        print('Elephant is packaged')

class Refrigerator:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.is_door_open = False

    def open_door(self):
        self.is_door_open = True
        print('Refrigerator door is opened')

    def close_door(self):
        self.is_door_open = False
        print('Close the refrigerator door')

    def put_elephant(self, elephant):
        if not self.is_door_open:
            self.open_door()
        if elephant.x < self.x and elephant.y < self.y and elephant.h < self.h:
            elephant.package()
            print('Elephant is in the fridge already')
        else:
            print('Refrigerator is too small to put elephant')
        self.close_door()

# Define element sizes
elephant_x = 5
elephant_y = 5
elephant_h = 5

# Define refrigerator sizes
refrigerator_x = 6
refrigerator_y = 6
refrigerator_h = 6

# Create instances of Elephant and Refrigerator classes
elephant = Elephant(elephant_x, elephant_y, elephant_h)
refrigerator = Refrigerator(refrigerator_x, refrigerator_y, refrigerator_h)

# Put the elephant in the refrigerator
refrigerator.put_elephant(elephant)

"""
1. The Elephant class contains the package method.

2. The Refrigerator class contains methods for opening and closing the door (open_door and close_door) 
as well as putting the elephant inside (put_elephant).

3. The logic to determine if the elephant fits into the refrigerator is now part of the put_elephant method.

4. We create instances of the Elephant and Refrigerator classes and use the put_elephant method to put the elephant into the refrigerator.
"""


class Car:
    def __init__(self, make, model, year, color, mileage, num):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.num = num

    def drive(self, distance):
        self.mileage += distance

    def paint(self, new_color):
        self.color = new_color

    def re_register(self, new_num):
        self.num = new_num

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage}")
        print(f"plate number: {self.num}")


# Test the Car class
car1 = Car("Toyota", "Camry", 2020, "Blue", 15000, "DUR 888")
car1.display_info()

car1.drive(100)
car1.paint("Red")
car1.display_info()
################
car1.re_register('DUR 666')
car1.display_info()



