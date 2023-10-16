# 0x0C. Python - Almost a circle

args/kwargs
JSON encoder and decoder
unittest module
Python test cheatsheet

1. **Unit Testing**:
    
    Unit testing is a software testing approach where individual components (units) of a software system are tested in isolation to ensure they work as expected. Here's a step-by-step guide to implementing unit testing in a large project:
    
    - **Choose a Testing Framework**: In Python, popular testing frameworks include `unittest`, `pytest`, and `nose`. Select one that suits your project.
        
    - **Organize Your Tests**: Create a separate directory for tests and organize test files with relevant names, e.g., `test_my_module.py`.
        
    - **Write Test Cases**: Create test cases for your functions and methods. Each test case should assert that a specific function or method behaves as expected. Use the testing framework's built-in assertion functions to check results.
        
    - **Test Fixture**: Use setup and teardown functions to set up the test environment and clean up afterward.
        
    - **Run Tests**: Execute your tests with the testing framework's runner. In most frameworks, you can run tests with a simple command, such as `pytest` or `python -m unittest discover`.
        
    - **Analyze Results**: Review the test results. If any tests fail, investigate the issues and make necessary code adjustments.
        
2. **Serialize and Deserialize a Class**:
    
    Serialization is the process of converting an object into a format that can be easily stored or transmitted, such as JSON or binary. Deserialization is the reverse process, converting serialized data back into an object.
    
    In Python, you can use the `pickle` module for binary serialization, and the `json` module for JSON serialization. Here's a basic example:
```python
import json

# Serialize a class instance to JSON
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_instance = MyClass("John", 30)
serialized = json.dumps(my_instance.__dict__)

# Deserialize JSON to a class instance
deserialized_data = json.loads(serialized)
new_instance = MyClass(**deserialized_data)

```

**Write and Read a JSON File**:

Writing data to a JSON file and reading from it is straightforward in Python:

Writing to a JSON file:
```python
import json

data = {"name": "John", "age": 30}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)

```
reading from a json file
```python
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

```
`*args` and 5. `**kwargs`:

`*args` and `**kwargs` are special syntax in Python used in function definitions to pass a variable number of non-keyword and keyword arguments, respectively.

- `*args`: Allows you to pass a variable number of non-keyword arguments to a function. They are collected into a tuple.
```python
def my_function(arg1, *args):
    print(arg1)
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4)

```
## `*args` (arbitary arguements)
- function that allows you to pass variable number of non keyworded arguements to a function
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15

```
`**kwargs`: Allows you to pass a variable number of keyword arguments to a function. They are collected into a dictionary.
```python
def my_function(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print(key, value)

my_function(1, name="John", age=30)

```
**Handling Named Arguments in a Function**:

To handle named arguments, simply define your function with named parameters:
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="John", age=30)

```
When you call the function, pass the arguments with their corresponding parameter names, making it clear what each value represents. This enhances code readability and allows you to pass arguments in any order.
## `**kwargs` (keyword arguements)
- a syntax that allows you to pass a variable number of keyworded arguements
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York

```

`*args` and `**kwargs` are special-magic features of Python. Think of a function that could have an unknown number of arguments. For example, for whatever reasons, you want to have function that sums an unknown number of numbers (and you don't want to use the built-in sum function). So you write this function:

```python
def sumFunction(*args):
  result = 0
  for x in args:
    result += x
  return result
```

and use it like: `sumFunction(3,4,6,3,6,8,9).`

`**kwargs` has a different function. With `**kwargs` you can give arbitrary keyword arguments to a function and you can access them as a dictonary.

```python
def someFunction(**kwargs):
  if 'text' in kwargs:
    print kwargs['text']
```

Calling someFunction(text="foo") will print foo.
## Order of using `*args`, `**kwargs` and formal args
- If you want to use to use all the three functions , the order is:
`some_func(fargs, *args, **kwargs)`
- Here's an example that uses 3 different types of parameters.

```python
def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print required_arg

    # args is a tuple of positional arguments,
    # because the parameter name has * prepended.
    if args: # If args is not empty.
        print args

    # kwargs is a dictionary of keyword arguments,
    # because the parameter name has ** prepended.
    if kwargs: # If kwargs is not empty.
        print kwargs

>>> func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: func() takes at least 1 argument (0 given)

>>> func("required argument")
required argument

>>> func("required argument", 1, 2, '3')
required argument
(1, 2, '3')

>>> func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")
required argument
(1, 2, '3')
{'keyword2': 'foo', 'keyword1': 4}
```
- `*args` = list of arguments - as positional arguments
- `**kwargs` = dictionary - whose keys become separate keyword arguments and the values become values of these arguments.
- You would use `*args` when you're not sure how many arguments might be passed to your function, i.e. it allows you pass an arbitrary number of arguments to your function. For example:

```python
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print( '{0}. {1}'.format(count, thing))
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage
```

Similarly, `**kwargs` allows you to handle named arguments that you have not defined in advance:

```python
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print( '{0} = {1}'.format(name, value))
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit
```
You can use these along with named arguments too. The explicit arguments get values first and then everything else is passed to `*args` and `**kwargs`. The named arguments come first in the list. For example:

```python
def table_things(titlestring, **kwargs)
```

You can also use both in the same function definition but `*args` must occur before `**kwargs`.

You can also use the `*` and `**` syntax when calling a function. For example:

```python
>>> def print_three_things(a, b, c):
...     print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))
...
>>> mylist = ['aardvark', 'baboon', 'cat']
>>> print_three_things(*mylist)
a = aardvark, b = baboon, c = cat
```

As you can see in this case it takes the list (or tuple) of items and unpacks it. By this it matches them to the arguments in the function. Of course, you could have a `*` both in the function definition and in the function call.

One place where the use of `*args` and `**kwargs` is quite useful is for subclassing.

```python
class Foo(object):
    def __init__(self, value1, value2):
        # do something with the values
        print value1, value2

class MyFoo(Foo):
    def __init__(self, *args, **kwargs):
        # do something else, don't care about the args
        print 'myfoo'
        super(MyFoo, self).__init__(*args, **kwargs)
```

This way you can extend the behaviour of the Foo class, without having to know too much about Foo. This can be quite convenient if you are programming to an API which might change. MyFoo just passes all arguments to the Foo class.

##  JSON encoder and decoder package in Python
- JSON stands for JavaScript Object Notation. It is a lightweight data interchange format. It is similar to pickle. However, pickle serialization is Python specific whereas JSON format is implemented by many languages. The json module in Python’s standard library implements object serialization functionality that is similar to pickle and marshal modules.

- Just as in pickle module, the json module also provides `dumps()` and `loads()` function for serialization of Python object into JSON encoded string, and dump() and load() functions write and read serialized Python objects to/from file.
### dumps()

This function converts the object into JSON format.

### loads()

This function converts a JSON string back to Python object.

Following example demonstrates basic usage of these functions.
```python
>>> import json
>>> data=['Rakesh',{'marks':(50,60,70)}]
>>> s=json.dumps(data)
>>> s
'["Rakesh", {"marks": [50, 60, 70]}]'
>>> json.loads(s)
['Rakesh', {'marks': [50, 60, 70]}]
```
Th dumps() function can take optional sort_keys argument. By default it is False. If set to True, the dictionary keys appear in sorted order in the JSON string.
```python
>>> data={"marks":50, "age":20, "rank":5}
>>> s=json.dumps(data, sort_keys=True)
>>> s
'{"age": 20, "marks": 50, "rank": 5}'
>>> json.loads(s)
{'age': 20, 'marks': 50, 'rank': 5}
```

The dumps() function has another optional parameter called indent which takes a number as value. It decides length of each segment of formatted representation of json string, similar to print output.
```python
>>> data = ['Rakesh',{'marks':(50,60,70)}]
>>> s = json.dumps(data, indent=2)
>>> print (s)
[
   "Rakesh",{
      "marks": [
         50,
         60,
         70
      ]
   }
]
```
The json module also has object oriented API corresponding to above functions. There are two classes defined in the module – JSONEncoder and JSONDecoder.

## JSONEncoder class

Object of this class is encoder for Python data structures. Each Python data type is converted in corresponding JSON type as shown in following table.
| Python Data Type                           | JSON Equivalent   |
| ----------------------------------------- | ----------------- |
| dict (object)                             | Object            |
| list, tuple (array)                       | Array             |
| str (string)                              | String            |
| int, float, int- & float-derived Enums    | Number            |
| True                                      | true              |
| False                                     | false             |
| None                                      | null              |

The JSONEncoder class is instantiated by JSONEncoder() constructor. Following important methods are defined in encoder class
```
- encode() − serializes Python object into JSON format
    
- iterencode() − Encodes the object and returns an iterator yielding encoded form of each item in the object.
    
- indent − Determines indent level of encoded string
    
- sort_keys − is either true or false to make keys appear in sorted order or not.
    
- Check_circular − if True, check for circular reference in container type object 

```

e.g 
```python
>>> e=json.JSONEncoder()
>>> e.encode(data)
'["Rakesh", {"marks": [50, 60, 70]}]'
```

## JSONDEcoder class

Object of this class helps in decoded in json string back to Python data truture. Main method in this class is decode(). Following example code retrieves Python list object from encoded string in earlier step.
```python
>>> d=json.JSONDecoder()
>>> d.decode(s)
['Rakesh', {'marks': [50, 60, 70]}]
```
## JSON with files/streams

The json module defines load() and dump() functions to write JSON data to a file like object – which may be a disk file or a byte stream and read data back from them.
## dump()

This function encodes Python object data in JSON format and writes it to a file. The file must be having write permission.
```python
>>> data=['Rakesh', {'marks': (50, 60, 70)}]
>>> fp=open('json.txt','w')
>>> json.dump(data,fp)
>>> fp.close()
```

## load()

This function loads JSON data from the file and constructs Python object from it. The file must be opened with read permission.
```python
>>> fp=open('json.txt','r')
>>> ret=json.load(fp)
>>> ret
['Rakesh', {'marks': [50, 60, 70]}]
>>> fp.close()
```
