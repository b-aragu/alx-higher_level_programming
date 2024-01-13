# README.md
-----------
# __`*args`__ and __`**kwargs`__

- Allows you to pass a variable number of arguments to a function
- __`*args`__ and __`**kwargs`__ are just conventions you can use other names only the asterisk matters

## __`*args`__
- Used to send non key-worded variable length argument list to the function
```run-python
def test_args(f_arg, *argv):
	print("first argument: ", f_arg)
	for arg in argv:
		print("other arguments: ", arg)
test_args("baragu", "antony", "gichuki")
```

## __`**kwargs`__
- Used to pass key-worded variable length of arguments to a function
- Use to handle named arguments to a function.
```run-python
def greet(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print(f"{key} == {value}")
greet(name="Baragu", age=19)
```

__`*args`__ for non key-worded arguments, __`**kwars`__ for key-worded arguments  
__Order of using all arguments is __ `def func(f_arg, *args, **kwargs)`

------------
# JSON
- javascript object notation is a lightweight data format used for data exchange 
#### Encoding `json` (serialization)

- use `json.dumps`

```run-python
import json
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], indent=4 ))
```

-  Write custom encoding function for classes 
#### Decoding __`json`__ 
- use `json.loads`
```run-python
import json
person = {
"name": "Baragu",
"age": 19,
"city": "Rongai",
"titles": ["student", "developer"]
}

personjson = json.dumps(person, indent=4)
print(personjson)
print(type(personjson))
print(json.loads(personjson))
print(type(json.loads(personjson)))
```

```run-python
import json
from json import JSONEncoder
class user:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
baragu = user("baragu", 19)
def encode_user(obj):
# implementing a custom encoder
	if isinstance(obj, user):
		return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
	else:
		raise TypeError("object is not json serializable")
baragujson = json.dumps(baragu, default=encode_user)
print(baragujson)

class user_encoder(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, user):
			return {
			'name': obj.name,
			'age': obj.age,
			obj.__class__.__name__: True
			}
		return JSONEncoder.default(self, obj)
baragucustom = json.dumps(baragu, cls=user_encoder)
# baragucustom = user_encoder().encode(baragu)
print(baragucustom)

def decode__user(dct):
	if user.__name__ in dct:
		return user(name=dct['name'], age=dct['age'])
	return dct
User = json.loads(baragucustom)
print(type(User))
print(User)
print(User.name)
```

-----
# Data marshalling
- Process that involves transforming the data representation or structure from one format to another typically for transimission or serialization.
- 

-----
# Unit Testing
__Test feature__ - representation needed to perform on or more test
__Test case__ - individual unit  of testing
__test suite__ -  a collection of test cases 
__test runner__ - a component which orchestrates the execution of tests and provides the outcomes to the user.
```run-python
import unittest
class TestStringMethods(unittest.TestCase):
	def test_upper(self):
		self.asserEqual('foo'.upper(), 'FOO')
	def test_isupper(self):
		self.assertTrue('FOO',isupper())
		self.asserFalse('Foo', isupper())
	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)
if __name__ == "__main__":
	unittest.main()
```
Skipping a test is simply a matter of using the skip decorator `@unittest.skip("info")`
