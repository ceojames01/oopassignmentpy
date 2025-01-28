class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

# Create instances of the classes
my_dog = Dog()
my_bird = Bird()
my_fish = Fish()

# Demonstrate polymorphism
for animal in [my_dog, my_bird, my_fish]:
    animal.move()