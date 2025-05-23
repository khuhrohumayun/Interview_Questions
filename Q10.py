   
    # Understanding Mixins in Object-Oriented Programming


"""
Problem: You want to gasp the concept of mixins in Object-Oriented
programming and understand their role in enhancing code reusability and 
extending class functionlity.

Solution: A mixin is a class that provides specific functionalities to be 
inherited by other classes, promoting code reusabilty and a modular approach to 
extending class behaviors.


Key characteristics of mixins include:

Single Responsibility: Mixins encapsulate a single, specific behavior.

Reusability: They are designed to be used in multiple classes, reducing code
duplication.

Inheritance: A class can inherit from one or more mixins to acquire their
functionality.

composition over inheritance: Mixins promote composition, allowing you to 
add specific behaviors without complex class hiearchies.

Conflict Resolution: When mixins define the same method or attribute,
conflict resolution mechanisms may be needed.


In python, mixins are used to enhance class through composition and are
commonly employed in the context of cooperative multiple inheritance,
leveraging the method resolution order (MRO) to resolve method calls
predictably.

Examples of minixs include loggableMixins for logging functionality or 
SerializableMixin for serialization capablities. By including these mixins in 
various classes, you can extend their functionality efficiently, following the 
principles of clean and modular code.

"""


        # Real-Life Analogy example

class Animal:
    def eat(self):
        print('Eating...')


# Mixin classes
class SwimmableMixin:
    def swim(self):
        print('Swimming...')

class FlyableMixin:
    def fly(self):
        print('Flying...')


# Duck has both behaviors
class Duck(Animal, SwimmableMixin, FlyableMixin):
    pass


duck = Duck()
duck.eat()
duck.swim()
duck.fly()


print('\n\n')
    
    # Another Example real life

class Car:
    def drive(self):
        print('Driving..')


# Mixins classes

class ElectricMixin:
    def charge(self):
        print("Charging...")

class MusicMixin:
    def play_music(slef):
        print('Music playing...')


# Create A tesla that inherits all methods
class Tesla(ElectricMixin, MusicMixin, Car):
    pass



tesla = Tesla()
tesla.drive()
tesla.play_music()
tesla.charge()