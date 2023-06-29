_Procedure oriented way of programming_ ~ designing programs under blocks of function
_Objected oriented way of programming_ ~ combining data and functionality and wrapping it inside something called an object

### analogy to understand OOP
Imagine you have a car manufacturing company. OOP is like designing and building cars using a blueprint.

In OOP, you have classes, which are like blueprints or templates for creating objects. Just like a blueprint specifies the structure and features of a car, a class defines the properties (attributes) and behaviors (methods) of an object.

For example, you can have a class called "Car" that defines what a car should have, such as color, model, and engine. This class acts as a blueprint for creating individual car objects.

Now, when you want to make a specific car, you create an instance (object) of the Car class, just as you would build a physical car based on a blueprint. Each car object will have its own unique characteristics, but they all follow the same structure defined by the Car class.

You can also have different classes for related objects. For instance, you might have a class called "Truck" that inherits from the Car class, but adds some specific features and behaviors unique to trucks.

In this way, OOP helps organize and manage code by breaking it down into modular and reusable components, just like how blueprints help streamline the car manufacturing process by providing a standardized way of building different cars.

### Properties vs. Getters and Setters
- Getters also known as accesor and setters also known as mutators
~ a method used for getting a value is decorated with ` @property`
~ The method which is to function as setter is decorated with `@<attribute.setter>`  
~ A `decorator` is a special construct in Python that allows modifying the behavior of a function or method. By using a decorator, it becomes possible to have methods with the same name but different parameter lists.
i.e 
```
class p:
	def __init__(self, x):
		self.x = x
	@property
	def x(self):
		return self.x
	@x.setter
	def x(self, x):
		self.x = x
```
- Two things are noteworthy: We just put the code line "self.x = x" in the `__init__` method and the property method x is used to check the limits of the values. The second interesting thing is that we wrote "two" methods with the same name and a different number of parameters "def x(self)" and "def x(self,x)". We have learned in a previous chapter of our course that this is not possible. It works here due to the decorating

## The `__init__`  method
It is a method which is immediately and automatically called after an instance has been created.
- mostly follows right after class header but can be anywhere in the class definition.
```
class name:
	def __init__(self, name=None):
		self.name  = name
	def say_hi(self):
		if self.name == None:
			print("hi , I have no name")
		else:
			print("Hey, my name is " + self.name)

 x = name()
 x.say_hi
 y = name("Baragu")
 y.say_hi
```

output:
```
Hi, I have no name
Hey, my name is Baragu
```

### Data Abstraction, Data Encapsulation, and Information Hiding
~ `encapsulation`  the bundling of data with methods that operates on the data 
~  `Information hiding` the principle that some internal fragmentation or data maybe hidden so that it cant  be accidentaly changed
`encapsulation` is accomplished by providing two kinds of method, the  [[#Properties vs. Getters and Setters|getter and setter method]]  
## `__str__`- and `__repr__`-Methods
- In Python, the `__str__` and `__repr__` methods are special methods that allow you to define how an object is represented as a string
1. `__str__` method: The `__str__` method is used to provide a human-readable string representation of an object. It is typically called by the built-in `str()` function or when you try to print an object. This method is meant to be used for display purposes and should return a string that provides a concise and informative representation of the object.
2. The `__repr__` method is used to provide a string representation of an object that is mainly meant for debugging and internal use. It is typically called by the built-in `repr()` function or when you try to display an object in the interactive console. This method should return a string that represents the object in such a way that it can be used to recreate the object.
_When to use str and repr?_ `_str_ ` is always the right choice if output is for user and should be nicely printed  `_repr_` is used for internal representation/

## Public, - Protected-, and Private Attributes
- In OOP there are 3 classifications of attributes
	1. Public Attribute can and should be used freely
	2. Protected attribute can be used but at your own risk, may only be used under certain conditions.
	3. Private attributes can only be used by owners i.e inside class definition itself
- Python uses special naming scheme to control their accessibility
	1. prefix an attribute name with a leading underscore `"_`"  to mark it as protected . It tells users of the class not to use this attribute unless, they write a subclass.
	2.  prefix an attribute name with two leading underscores `"__"` to mark it as private. The attribute is now inaccessible and invisible from outside. It's neither possible to read nor write to those attributes except inside the class definition itself.
	3. a public attribute has no leading underscore
i.e 
```
class attribue:
	def __init__(self):
		self.pub = "I am a public attribute"
		self._prot = "I am a protected attribute"
		self.__priv = "I am a private attribute"
x = attribue()
x.pub # output: I am a public attribute
x._prot # output: I am a protected attribute
x.__priv /* output:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-f75b36b98afa> in <module>
----> 1x.__priv
AttributeError: 'A' object has no attribute '__priv'
*/
```
- note in `x.__priv` the error message looks like a lie because There is such an attribute, but we are told that there isn't. This is perfect information hiding. Telling a user that an attribute name is private, means that we make some information visible, i.e. the existence or non-existence of a private variable.

### Destructor
- called when an instance is to be destroyed and there is no reference to the instance , use `__del__`
i.e 
```
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print ("Robot has been destroyed")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
```
Output:
```
Tik-Tok has been created!
Jenkins has been created!
Deleting x
Deleting z
Robot has been destroyed
Robot has been destroyed
```
