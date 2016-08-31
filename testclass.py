# Test script from book Python Crash Course
# From Chapter 9 - Classes

# First example is the dog class

class dog():
    """A basic class that models the dog"""
    current_status = ()

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        self_maxweight = 40

    def sit(self):
        """Dog responds to sit."""
        print(self.name.title() + " is now sitting.")
        current_status = ('Sitting')

    def rollover(self):
        """Dog responds to roll over."""
        print(self.name.title() + " rolled over!")
        current_status = ('Standing')

my_dog = dog('Alex', 13)
your_dog = dog('Jed',7)
print("My dog's name is " + my_dog.name.title() + ".")
print(my_dog.name.title() + " is " + str(my_dog.age) + " years old.")
my_dog.sit()
your_dog.sit()
print (my_dog.current_status)



