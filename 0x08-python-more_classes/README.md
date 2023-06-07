# Python Classes and Objects

## Introduction

Python is an awesome programming language known for its simplicity and readability. It provides powerful object-oriented programming (OOP) capabilities, allowing developers to structure their code around objects and classes.

## Symbols Used

- `__repr__`: The special method used to define a string representation of an object that can be used to recreate the object.
- `__str__`: The special method used to define a human-readable string representation of an object.
- `self`: A special parameter representing the instance of a class.
- `__init__`: The special method (constructor) that initializes an object when it is created.
- Public attribute: An attribute accessible from anywhere.
- Protected attribute: An attribute intended to be used within the class and its subclasses (denoted by a single leading underscore).
- Private attribute: An attribute meant to be used only within the defining class (denoted by a double leading underscore).
- Method: A function defined within a class that operates on instances or the class itself.
- Data abstraction: Hiding complex implementation details and exposing only essential information to the user.
- Data encapsulation: Bundling related attributes and methods within a class and providing well-defined interfaces for accessing them.
- Information hiding: Restricting access to certain attributes or methods to maintain data integrity and encapsulation.
- Property: A way to define attribute accessors and mutators with the appearance of ordinary attributes.
- Class attribute: A variable defined within a class, shared among all instances of the class.
- Object attribute: An attribute specific to an individual instance.
- Class method: A method defined within a class that operates on the class itself.
- Static method: A method defined within a class that is independent of instances or the class.
- `__dict__`: The attribute containing the namespace of a class or an instance.
- Attribute lookup: The process of searching for an attribute in an object's or class's namespace.
- `getattr()`: The function used to dynamically retrieve the value of an attribute.

## Why Python Programming is Awesome

Python is awesome because of its simplicity, readability, and versatility. It has a vast collection of libraries and frameworks that make development faster and easier. Python's syntax is clean and concise, promoting code readability and maintainability. Moreover, Python's extensive support for OOP allows for modular and reusable code.

## What is OOP

Object-oriented programming (OOP) is a programming paradigm that structures code around objects, which are instances of classes. It promotes modularity, reusability, and code organization by encapsulating data and behavior into objects. OOP concepts include abstraction, encapsulation, inheritance, and polymorphism.

## "First-Class Everything"

Python follows the principle of "first-class everything," treating functions, methods, and classes as first-class citizens. This means that they can be assigned to variables, passed as arguments to functions, and returned as values from functions.

## What is a Class

A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class will have.

## What is an Object and an Instance

An object is an instance of a class. It is a concrete entity that contains data and behaviors defined by its class. Creating an object is called instantiation, and each object is considered an instance of its class.

## Difference Between a Class and an Object or Instance

A class is a blueprint or template that defines the structure and behavior of objects. It is a general concept. An object or instance, on the other hand, is a specific entity created based on a class. It represents a concrete realization of the class with its own set of attributes and values.

## What is an Attribute

An attribute is a piece of data associated with an object. It represents the state or characteristics of an object. Attributes can be variables or properties defined within a class.

## Public, Protected, and Private Attributes

- Public attributes are accessible from anywhere. They can be accessed and modified directly.
- Protected attributes are intended to be used within the class and its subclasses. They are denoted by a single leading underscore (e.g., `_attribute`).
- Private attributes are meant to be used only within the defining class. They are denoted by a double leading underscore (e.g., `__attribute`).

## What is `self`

`self` is a special parameter that represents the instance of a class. It allows accessing and manipulating the instance's attributes and methods within the class.

## What is a Method

A method is a function defined within a class that operates on instances or the class itself. It represents the behavior or actions that objects of the class can perform.

## The Special `__init__` Method

The `__init__` method, also known as the constructor, is a special method that initializes an object when it is created. It is called automatically when an object is instantiated from a class. It allows setting initial values for the object's attributes.

## Data Abstraction, Data Encapsulation, and Information Hiding

- Data abstraction is the process of hiding complex implementation details and exposing only essential information to the user. It allows users to interact with objects using simplified interfaces.
- Data encapsulation is the bundling of related attributes and methods within a class. It promotes code organization, modularity, and reusability.
- Information hiding is the practice of restricting access to certain attributes or methods to maintain data integrity, encapsulation, and modularity.

## Property

A property provides a way to define attribute accessors and mutators with the appearance of ordinary attributes. It allows controlling attribute access and providing additional functionality when getting or setting values.

## Difference Between an Attribute and a Property in Python

Attributes are data stored within an object, while properties are methods that define access to those attributes. Properties enable attribute access control and perform additional actions when getting or setting attribute values.

## The Pythonic Way to Write Getters and Setters

In Python, the use of explicit getters and setters is not common. Instead, properties are preferred to provide attribute access and modification methods. Properties can be defined using the `@property`, `@attribute_name.setter`, and `@attribute_name.deleter` decorators.

## The Special `__str__` and `__repr__` Methods

- The `__str__` method returns a human-readable string representation of the object. It is used for display purposes.
- The `__repr__` method returns a string representation that can be used to recreate the object. It provides an unambiguous representation.

## Difference Between `__str__` and `__repr__`

- `__str__` is intended for a human-readable representation, while `__repr__` is used to create an unambiguous string representation for recreating the object.
- `__str__` is called by the `str()` function and is used for display purposes.
- `__repr__` is called by the `repr()` function and is used for debugging and development purposes.

## Class Attributes

Class attributes are variables defined within a class but outside any methods. They are shared among all instances of the class and can be accessed through both the class and its instances.

## Difference Between Object Attributes and Class Attributes

- Object attributes are specific to individual instances and are unique to each object.
- Class attributes are shared among all instances of the class and can be accessed through both the class and its instances.

## Class Methods

Class methods are defined within a class and operate on the class itself rather than on instances. They are bound to the class and can access class attributes but not instance attributes.

```class Car:
    wheels = 4  # Class attribute

    @classmethod
    def get_wheels(cls):
        return cls.wheels

print(Car.get_wheels())  # Output: 4
