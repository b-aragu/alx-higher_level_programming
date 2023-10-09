#### Inheritance
- Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class by inheriting properties and behaviors (attributes and methods) from an existing class. Inheritance promotes code reuse and the creation of a hierarchy of classes, which makes it easier to model and manage complex systems.
##### Basic key concept
1. **Base Class (Parent Class or Superclass):** The class from which properties and behaviors are inherited is called the base class, parent class, or superclass. It serves as the blueprint for other classes.
    
2. **Derived Class (Child Class or Subclass):** The class that inherits properties and behaviors from the base class is called the derived class, child class, or subclass. It can add additional attributes and methods or override existing ones.
3. **Access to Parent Class Members:** In a derived class, you can access the attributes and methods of the base class using dot notation example 
```
class BaseClass:
    def __init__(self):
        self.base_attribute = "I am from the base class"

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()  # Call the base class constructor
        self.derived_attribute = "I am from the derived class"

obj = DerivedClass()
print(obj.base_attribute)    # Access base class attribute

```

4. **Method Overriding:** A derived class can provide its own implementation for a method inherited from the base class. This is called method overriding. When you call the overridden method on an instance of the derived class, the derived class's implementation is executed. This allows you to customize the behavior of the inherited method in the context of the derived class. ```

```
class BaseClass:
    def show_info(self):
        print("I am from the base class")

class DerivedClass(BaseClass):
    def show_info(self):
        print("I am from the derived class")

obj = DerivedClass()
obj.show_info()  # Calls the overridden method in the derived class

```

5.  **Multiple Inheritance:** Some programming languages, including Python, support multiple inheritance, which allows a class to inherit from more than one base class. However, you should use multiple inheritance carefully to avoid ambiguity and complex class hierarchies.
- The capability of a class to inherit the properties of another class
- It represent real world relationship well
- It provide code re-usability
- It is transitive in nature
- It offers simple understandable model structure
- Less development and maintenance

###### Inheritance syntax
The syntax of inheritance is 
```
class baseclass:
	body

class derivedclass(baseclass):
	body
```

- parent class - class whose properties are inherited by the child class.
- Example of inheritance 
```
# A Python program to demonstrate inheritance
class Person:
   
  # Constructor
  def __init__(self, name, idn):
    self.name = name
    self.idn = idn
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.idn)
 
 # creating a sub class
class Emp(Person):

    def print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# calling child class function
Emp_details.print()

```

1. **Why Python programming is awesome:**
    
    - Python is known for its simplicity and readability, making it an excellent choice for beginners and experienced developers.
    - It has a vast standard library with built-in modules for various tasks.
    - Python is a versatile language used in web development, data analysis, machine learning, and more.
    - It supports multiple programming paradigms, including object-oriented, functional, and procedural programming.
    - Python has a strong and active community that contributes to its growth and provides extensive documentation and third-party libraries.
2. **What is a superclass, base class, or parent class:**
    
    - A superclass, base class, or parent class is a class that is extended or inherited by another class (the subclass or child class). The superclass defines common attributes and methods that are shared by its subclasses.
3. **What is a subclass:**
    
    - A subclass, also known as a derived class or child class, is a class that inherits attributes and methods from a superclass or base class. It can also add new attributes and methods or override existing ones.
4. **How to list all attributes and methods of a class or instance:**
    
    - You can use the `dir()` function to list all attributes and methods of a class or instance. For example: `print(dir(ClassOrInstance))`.
5. **When can an instance have new attributes:**
    
    - Instances in Python can have new attributes assigned at any time. You can add new attributes to an instance dynamically by simply assigning a value to them. For example: `obj.new_attribute = 'new_value'`.
6. **How to inherit a class from another:**
    
    - In Python, you inherit a class from another by including the name of the base class in parentheses when defining the derived class. Example: `class DerivedClass(BaseClass):`.
7. **How to define a class with multiple base classes:**
    
    - To define a class with multiple base classes, you use a comma-separated list of base classes within parentheses when defining the class. Example: `class DerivedClass(BaseClass1, BaseClass2):`.
8. **What is the default class every class inherits from:**
    
    - In Python, the default base class for all classes is called `object`. If you don't explicitly specify a base class when defining a class, it implicitly inherits from `object`.
9. **How to override a method or attribute inherited from the base class:**
    
    - To override a method or attribute inherited from the base class, you define the same method or attribute in the subclass with a new implementation. The subclass's method or attribute will be used when called on instances of the subclass.
10. **Which attributes or methods are available by inheritance to subclasses:**
    
    - Subclasses inherit all attributes and methods (both public and protected) from the base class except for attributes and methods that are explicitly marked as private (usually with a leading underscore).
11. **What is the purpose of inheritance:**
    
    - The purpose of inheritance is to promote code reuse, create a hierarchy of classes with shared functionality, and allow for customization and extension of classes. It helps organize and structure code in a more modular and maintainable way.
12. **What are, when and how to use isinstance, issubclass, type, and super built-in functions:**
    
    - `isinstance`: Used to check if an object is an instance of a specific class or a tuple of classes. Example: `isinstance(obj, MyClass)`.
    - `issubclass`: Used to check if a class is a subclass of another class. Example: `issubclass(SubClass, BaseClass)`.
    - `type`: Returns the type of an object. Example: `type(obj)`.
    - `super`: Used to call a method from a base class in the context of a subclass. Example: `super().method_name()`.

#### dir()
- It is used to list name of attributes including methods 
