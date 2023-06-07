## Python Classes and Objects
Python programming offers a powerful object-oriented programming (OOP) paradigm, making it an awesome language for developing robust and modular applications. This document provides an overview of Python classes and objects, highlighting key concepts and features.

## Table of Contents
- Introduction
- Classes and Objects
- First-Class Everything
- Class
- Object and Instance
- Attributes
- Public, Protected, and Private Attributes
- Self
- Methods
- The __init__ Method
- Data Abstraction, Encapsulation, and Information Hiding
- Property
- Difference Between Attribute and Property
- Getters and Setters
- The` __str__` and `__repr__` Methods
- Difference Between `__str__` and `__repr__`
- Class Attributes
- Difference Between Object and Class Attributes
- Class Methods
- Static Methods
- Dynamically Creating Attributes
- Binding Attributes
- `__dict__` of a Class and an Instance
`Attribute Lookup
`Using the getattr() Function
## Introduction<a name="introduction"></a>
Python's OOP capabilities allow for organizing code into reusable and modular structures. Key concepts in OOP include classes, objects, methods, attributes, and encapsulation.

## Classes and Objects<a name="classes-and-objects"></a>
### First-Class Everything<a name="first-class-everything"></a>
In Python, everything is considered an object, and this concept is known as "first-class everything." It means that objects can be assigned to variables, passed as arguments, returned from functions, and stored in data structures.

```
# Assigning an object to a variable
x = 10

# Passing an object as an argument
def multiply_by_two(num):
    return num * 2

result = multiply_by_two(x)

# Returning an object from a function
def create_list():
    return [1, 2, 3]

my_list = create_list()

# Storing objects in a data structure
my_list = [1, 2, 3] ```
## Class<a name="class"></a>
A class is a blueprint or template that defines the structure and behavior of objects. It encapsulates attributes (data) and methods (functions) that the objects can possess.

```
class Car:
    pass
```
## Object and Instance<a name="object-and-instance"></a>
An object is an instance of a class. It represents a specific entity based on the class blueprint. When an object is created, memory is allocated to store its data.

```
# Creating an object of the Car class
my_car = Car()
```
### Attributes<a name="attributes"></a>
Attributes are the properties or characteristics associated with a class or object. They can be variables or constants and can hold any data type, such as integers, strings, or even other objects.

```
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model
```
### Public, Protected, and Private Attributes<a name="public-protected-and-private-attributes"></a>
In Python, attribute visibility can be controlled using naming conventions. Public attributes are accessible from anywhere. Protected attributes have a single leading underscore and are intended to be used within the class and its subclasses. Private attributes have a double leading underscore and are meant to be used only within the defining class.
```
class Car:
    wheels = 4       # Public attribute
    _fuel_capacity = 50    # Protected attribute
    __engine_type = "Petrol"   # Private attribute

    def __init__(self, make, model):
        self.make = make    # Public instance attribute
        self._model = model   # Protected instance attribute
        self.__year = 2022    # Private instance attribute
```
### Self<a name="self"></a>
self is a special parameter that represents the instance of the class. It allows accessing the instance's attributes and methods within the class.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_full_name(self):
        return f"{self.make} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.get_full_name())  # Output: Toyota Corolla
```
### Methods<a name="methods"></a>
Methods are functions defined within a class and operate on class instances or the class itself. They can access and modify the object's attributes.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_full_name(self):
        return f"{self.make} {self.model}"

    def start_engine(self):
        print("Engine started")

my_car = Car("Toyota", "Corolla")
print(my_car.get_full_name())  # Output: Toyota Corolla
my_car.start_engine()  # Output: Engine started
```
### The `__init__` Method<a name="the-__init__-method"></a>
The `__init__ `method is a special method (constructor) that gets called when an object is created from a class. It initializes the object's attributes and performs any necessary setup.

```
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Toyota", "Corolla", 2022)
```
### Data Abstraction, Encapsulation, and Information Hiding<a name="data-abstraction-encapsulation-and-information-hiding"></a>
Data abstraction is the process of hiding complex implementation details and exposing only essential information to the user. Encapsulation is achieved by bundling related attributes and methods within a class, making them accessible only through well-defined interfaces.

```
class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute

    def get_full_name(self):
        return f"{self._make} {self._model}"
```
### Property<a name="property"></a>
Properties provide a way to define attribute accessors and mutators with the appearance of ordinary attributes. They allow controlling attribute access and provide additional functionality when getting or setting values.

```
class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @make.setter
    def make(self, make):
        self._make = make

    @model.setter
    def model(self, model):
        self._model = model

my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota
my_car.make = "Honda"
print(my_car.make)  # Output: Honda
```
### Difference Between Attribute and Property<a name="difference-between-attribute-and-property"></a>
Attributes are data stored within an object, while properties are methods that define access to those attributes. Properties enable attribute access control and perform additional actions when getting or setting attribute values.

### Getters and Setters<a name="getters-and-setters"></a>
In Python, the use of explicit getters and setters is not common. Instead, properties are preferred to provide attribute access and modification methods.

### The `__str__` and `__repr__` Methods<a name="the-__str__-and-__repr__-methods"></a>
The `__str__` method returns a human-readable string representation of the object, while the __repr__ method returns a string representation that can be used to recreate the object. Both methods are used for different purposes and can be overridden to customize the string representation.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"Car: {self.make} {self.model}"

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}')"

my_car = Car("Toyota", "Corolla")
print(str(my_car))  # Output: Car: Toyota Corolla
print(repr(my_car))  # Output: Car(make='Toyota', model='Corolla')
```
### Difference Between __str__ and __repr__<a name="difference-between-__str__-and-__repr__"></a>
The `__str__` method is intended for a human-readable representation, while __repr__ aims to provide an unambiguous string representation that can be used to recreate the object.

### Class Attributes<a name="class-attributes"></a>
Class attributes are variables defined within a class but outside any methods. They are shared among all instances of the class and can be accessed through both the class and its instances.

```
class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make
        self.model = model

print(Car.wheels)  # Output: 4

my_car = Car("Toyota", "Corolla")
print(my_car.wheels)  # Output: 4
```
### Difference Between Object and Class Attributes<a name="difference-between-object-and-class-attributes"></a>
Object attributes are specific to individual instances and are unique to each object. Class attributes, on the other hand, are shared among all instances of the class and are accessed through both the class and its instances.

### Class Methods<a name="class-methods"></a>
Class methods are defined within a class and operate on the class itself rather than on instances. They are bound to the class and can access class attributes but not instance attributes.

```
class Car:
    wheels = 4  # Class attribute

    @classmethod
    def get_wheels(cls):
        return cls.wheels

print(Car.get_wheels())  # Output: 4
```
### Static Methods<a name="static-methods"></a>
Static methods are defined within a class but do not operate on instances or the class itself. They are independent of the class and can be called without instantiating the class.

```
class MathUtils:
    @staticmethod
    def add_numbers(x, y):
        return x + y

result = MathUtils.add_numbers(5, 3)
print(result)  # Output: 8
```
### Dynamically Creating Attributes<a name="dynamically-creating-attributes"></a>
In Python, attributes can be dynamically created for existing instances of a class by simply assigning a value to a new attribute name.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
my_car.color = "Red"  # Dynamically adding a new attribute
print(my_car.color)  # Output: Red
```
### Binding Attributes<a name="binding-attributes"></a>
Attributes can be bound to both objects and classes. Bound attributes are accessed using dot notation and are resolved based on the object's or class's attribute lookup.

### `__dict__` of a Class and an Instance<a name="__dict__-of-a-class-and-an-instance"></a>
The `__dict__` attribute of a class contains a dictionary that holds the attributes defined within the class. For an instance, __dict__ contains the instance's attributes along with the attributes inherited from its class.

```
class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")

print(Car.__dict__)  # Output: {'__module__': '__main__', 'wheels': 4, '__init__': <function Car.__init__ at 0x000001>, ...}
print(my_car.__dict__)  # Output: {'make': 'Toyota', 'model': 'Corolla'}
```
### Attribute Lookup<a name="attribute-lookup"></a>
When accessing an attribute on an object or class, Python performs an attribute lookup. It searches for the attribute in the object's or class's namespace, including inherited attributes.

### Using the getattr() Function<a name="using-the-getattr-function"></a>
The getattr() function allows retrieving the value of an attribute dynamically by providing the object and attribute name as arguments. It returns the attribute value if found or raises an exception if the attribute is not found.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
make = getattr(my_car, "make")
print(make)  # Output: Toyota
```
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
