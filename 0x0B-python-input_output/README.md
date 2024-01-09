# Reading and writing files 
- `open()` returns a file object `open(filename, mode, encoding=None)`
	if encoding isn't specified the default is platform dependent.
- `with` - file automatically closed after it suites finishes 
	```python
	with open(filename, 'w', encoding="utf-8") as f:
	    read_data = f.read()
	```

	If not using with keyword use `f,close()` to close the file 

#### Methods of file objects
__`f.read(size)`__ to read file content , size is an optional numeric argument.
	returns empty string if end of file has been reached.
__`f.readline()`__ reads a single line from the file.

__`looping`__  Memory efficient, fast and leads to simple code
```python
for line in f:
	print(line, end='')
```

__`list(f)`__ or __`readlines()`__  Reads all the lines of a file in a list
__`f.write(string)`__ Write the content of a string to file returning the number of of characters written.
__`f.tell()`__ Returns an integer giving the file objects current position in the file represented as number of bytes from the beginning of the file when in binary mode and opaque when in text mode

__`f.seek(offset, whence)`__ - to change the file object position.

------
# Saving Structured data with json
-----
#### JSON

- Take python data hierachies and converts them to string representation __serializing__
```python
import json
x = [1, 'simple, 'list]
json.dumps(x) # convert obj x to json string representation
# output '[1, "simple], "list'
```
__deserializing__ - decodes the json object to a python string representation
```python
import json
json.load(x)
```

-----
#### PYINPUTPLUS Module for input validation
 - contains function similar to `input()` for several kinds of data
install it separately using  `pip install --user pyinputplus`
__`inputstr()`__ like builtin `input()` but has pyinputplus general fetures
__`inputNum()`__ Ensure user enters a number and returns an int or float
__`inputchoice()`__ Ensures the user enters one of the provided choices
__`inputMenu`__ - provide menu with lettered or numbered options
__`inputDatetime()`__ users enter a date and time 
__`inputEmail() users enters a valid email
__`inputPassword`__ displays `*` as users enters password 
