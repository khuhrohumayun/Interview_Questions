    
        # Introspection and Reflection

"""
Problem: You want to understand the concepts of introspection and
reflection in programming and determine if Python supports these features.

Solution: Introspection (or reflection) is the ability of a programming
language to examine, analyze, and manipulates its own structures and objects 
at runtime. Python strongly supports introspection, which means you can 
inspect and manipulate various aspects of objects, classes and modules 
during runtime



Here are some ways Pythons supports introspection:


Getting Object Type: You can use the type() function to determine the type of
an object.


Getting Object's Attributes: The dir() funciton allows you to retrieve the
an object.

Inspecting Documentation: You can access docstrings using the .__doc__
attribute.

Getting Object's Base Classes: The .__bases__ attribute helps inspect the
base classes of a class.

Dynamic Module Import: Python allows dynamic module import using 
importlib or __import__.

Dynamic Function/Class Creation: You can dynamically create functions and 
classes using type() and metaprogramming techniques.

Checking for Attribute: The hasattr() funtion checks if an object has a
specific attribute or method.

Callable Check: The callable() function verifies if an object can be called like a
function.
"""


  # Example of Introspection 
class Person:
    """This class represents a person."""
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, Iam {self.name}"
    
p = Person("Ali")

print(type(p))    # <class '__main__.Person'>
print(dir(p))     # List of all properties/methodds of p
print(hasattr(p, "name")) # True
print(getattr(p, "name")) # Ali
print(callable(p.greet))  # True
print(p.__doc__)          # This class represents a person. 




  # Example of Reflection
  # Creating a new class dynamically
NewClass = type("NewClass", (), {'x': 5})
obj = NewClass()
print(obj.x) # 5