# animals.py
import random

class Animal:
    """Parent class representing an animal."""

    def __init__(self, name, species):
        """Initializes an Animal object."""
        self.name = name
        self.species = species

    def make_sound(self):
        """Prints a generic animal sound."""
        print("Generic animal sound.")

    def move(self):
        """Prints a generic movement."""
        print("Animal walks.")

class Dog(Animal):
    """Child class representing a dog."""
    dog_breeds = ["Labrador Retriever", "Pitbull", "Shiba Inu", "German Shepherd"]
    def __init__(self, name, breed=None):
        """Initializes a Dog object."""
        if breed is None:
            breed = random.choice(self.dog_breeds)
        super().__init__(name, species="Dog")  # Call parent's __init__
        self.breed = breed

    def make_sound(self):
        """Prints the dog's bark."""    
        print("Bark!")

    def move(self):
        print("Dog catches a ball.")

class Cat(Animal):
    """Child class representing a cat."""
    cat_colors = ["Black", "White", "Orange", "Brown"]

    def __init__(self, name, color=None):
        """Initializes a Cat object."""
        if color is None:
            color = random.choice(self.cat_colors)
        super().__init__(name, species="Cat")  # Call parent's __init__
        self.color = color

    def make_sound(self):
        """Prints the cat's meow."""
        print("Meow!")

    def move(self):
        print("Cat scurries quickly.")

class Bird(Animal):
    """Child class representing a Bird."""
    bird_wingspans = ["10 inches", "15 inches", "20 inches", "25 inches"]
    
    def __init__(self, name, wingspan=None):
        """Initializes a bird object"""
        if wingspan is None:
            wingspan = random.choice(self.bird_wingspans)

        super().__init__(name, species="Bird")
        self.wingspan = wingspan

    def make_sound(self):
        print("Chirp!")

    def move(self):
        print("Bird talks.")

class Reptile(Animal):
    """Child Class representing a reptile"""
    reptile_scale_types = ["Diamond", "Spiral", "Lizard", "Crocodile"]
    
    def __init__(self, name, scale_type=None):
        """Initializes a reptile object"""
        if scale_type is None:
            scale_type = random.choice(self.reptile_scale_types)
       
        super().__init__(name, species = "Reptile")
        self.scale_type = scale_type

    def make_sound(self):
        print("Hiss!")

    def move(self):
        print("Reptile slithers.")

# Example Usage (for testing):
if __name__ == "__main__":
    animal = Animal("Generic Animal", "Unknown")
    dog = Dog("Fido")
    puppy = Dog("Dude")
    cat = Cat("Fluffy")
    bird = Bird("Chica")
    reptile = Reptile("Python")

    animal.make_sound()
    dog.make_sound()
    cat.make_sound()
    bird.make_sound()
    reptile.make_sound()

    animal.move()
    dog.move()
    cat.move()
    bird.move()
    reptile.move()

    print(dog.breed)
    print(puppy.breed)
    print(cat.color)
    print(bird.wingspan)
    print(reptile.scale_type)