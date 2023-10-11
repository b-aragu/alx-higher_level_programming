# Python - Input/ Output
- open() returns a file object
`open(filename, mode, encoding=None)`
`filename` ~ the name of the file e.g. file.txt
`mode` - can either be read 'r', write 'w', append 'a', adding 'b' to the modes open file in binary mode
- with keyword is used to explicitly manage resources that needs to be opened and closed e.g files
The general syntax is `with expression as target`
```python
with open("example.txt, "r") as file:
	content = file.read()
	print(content)
```
while the block is executed the file is automatically closed. 
- you can also close a file using close(), when you attempt to use the file object after closing it  will fail.

### Methods of file object
- lets create a file object f
`f = open("file", "a", encoding="utf-8")
- To _read_ file content use `f.read(size` size is an optional numerical arguement
- To read a single line from a file use `f.readline()`
- `f.write(string)` writes the content of string to the file returning number of characters written
	e.g `>>> f.write(This is a test\n)` will output 15
- `f.tell()` returns an integer giving the objects current position i n the file rep as number of bytes from begining of file when in binary mode and an  opaque number when in text mode
- To change file position use `f.seek(offset, whence)`
- Other objects need to be converted  either to a string or byte object before writing them
	```python
	value = ('the answer', 42)
	s = str(value) # converts the tuple to string
	f.write(s) # outputs 18
  ```
- `io.StringIO` lets you treat a string as a text file. There’s also a io.BytesIO class, which lets you treat a byte array as a binary file.
- The `gzip` module lets you create a stream object for reading or writing a gzip-compressed file.
example: 
```python
import gzip 
with gzip.open('out.log.gz', mode='wb') as z_file: 
	z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
	exit()
```

### Saving Structured data with _json_
- serializing - Taking complex python data hierachies  and converting them to strings 
- Javascript object notation is a popular data interchange format
- To save structured data using JSON, you can follow these general steps:
1. Prepare your data in a structured format, such as a dictionary or a list of dictionaries, in your programming language of choice. Ensure that the data is compatible with JSON data types (strings, numbers, booleans, lists, dictionaries).
    
2. Import the JSON library or module provided by your programming language. For example, in Python, you can import the `json` module.
    
3. Use the appropriate function or method provided by the JSON library to convert your data into a JSON string. In Python's `json` module, you can use the `json.dumps()` function to serialize the data.
    
4. Open a file for writing in your preferred mode (e.g., "w" for writing) using the built-in file handling functions or classes provided by your programming language.
5. Write the JSON string to the file using the file handling functions or methods. In Python, you can use the `write()` method of the file object.
6. Close the file to ensure that the changes are saved properly.

e.g. 
```python
import json
x = [1, 'simple', 'list']
json.dumps(x)
```

### Raising and handling multiple unrelated exceptions
- `ExceptionGroup` wraps a list of exceptions instances so they can be raised together
- `except*` selectively handle only the exception in the group that match a certain type.

### Enriching exception with Notes
Exceptions have a method `add_note(note)` that accepts a string and add the exceptions notes list `exception.add_note('note')`

### JSON encoder and decoder
In programming, a JSON encoder and decoder are components that facilitate the conversion of data between JSON format and the data structures of a programming language. These components are typically provided by libraries or modules specific to the programming language being used. Here's an explanation of JSON encoders and decoders:

JSON Encoder: A JSON encoder takes data from a programming language's data structure (such as objects, lists, or dictionaries) and converts it into a JSON-formatted string. The encoder ensures that the data is formatted according to the JSON syntax rules, which include using double quotes for strings, representing numbers, booleans, and null appropriately, and structuring objects and arrays. The resulting JSON string can be used for data transmission, storage, or interoperability between different systems.

JSON Decoder: A JSON decoder, on the other hand, performs the reverse operation. It takes a JSON-formatted string and converts it into the corresponding data structure of the programming language. The decoder parses the JSON string, validates its syntax, and recreates the original data structure using the appropriate data types. This allows the program to work with the data in its native format for further processing or manipulation.

Most programming languages provide built-in or third-party libraries for JSON encoding and decoding. Here are some examples:

- Python: The `json` module in Python provides the `json.dumps()` function for encoding data into JSON format and the `json.loads()` function for decoding JSON into Python objects.
    
- JavaScript: In JavaScript, the `JSON` object has methods like `JSON.stringify()` for encoding data to JSON and `JSON.parse()` for decoding JSON into JavaScript objects.
    
- Java: Java offers the `org.json` package, which includes the `JSONObject` class for encoding Java objects to JSON using `toString()` and the `JSONArray` class for handling JSON arrays. The `org.json` package also provides methods like `JSONObject.fromObject()` for decoding JSON into Java objects.
    
- PHP: PHP provides the `json_encode()` function for encoding PHP arrays and objects into JSON and the `json_decode()` function for decoding JSON into PHP arrays or objects.
    

These are just a few examples, and other programming languages also have similar JSON encoding and decoding capabilities. These functionalities make it convenient to work with JSON data and facilitate interoperability between different systems and languages.

#### Standard Input, output and errors
- standard output (stdout) and standard error (stderr) are pipes built for Unix-like systems.
- When you call the `print()` the thing you are printing is sent to the `stdout` pipe.
- When your program crashes and prints out a traceback, it goes to the `stderr` pipe.
- `stdout` and `stderr` are defined in the __`sys`__ module and they are stream objects.
- In the simplest case, sys.stdout and sys.stderr send their output to the same place: the Python IDE (if you’re in one), or the terminal (if you’re running Python from the command line). Like standard output, standard error does not add carriage returns for you. If you want carriage returns, you’ll need to write carriage return characters. 
- `sys.stdout` and `sys.stderr` are stream objects, but they are write-only. Attempting to call their read() method will always raise an `IOError`.
- # Python Programming: File Handling, JSON, and Serialization

Python is considered awesome for various reasons, including its simplicity, readability, extensive libraries and frameworks, community support, and cross-platform compatibility. In this guide, we'll cover essential aspects of Python programming related to file handling, JSON, serialization, and deserialization.

## File Handling

### How to Open a File

You can open a file in Python using the `open()` function. You need to specify the file path and the mode in which you want to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending, etc.).

```python
with open('file.txt', 'r') as file:
   # File operations go here
```


### How to Write Text in a File

To write text to a file, open it in write ('w') or append ('a') mode and use the `write()` method or the `writelines()` method to write content.
```python
with open('file.txt', 'w') as file:
   file.write('Hello, World!')

```

### How to Read the Full Content of a File

You can read the full content of a file using the `read()` method, which reads the entire file into a string.
```python
with open('file.txt', 'r') as file:
   content = file read()

```

### How to Read a File Line by Line

To read a file line by line, you can use a `for` loop to iterate through the file object. Alternatively, you can use the `readline()` method.
```python
with open('file.txt', 'r') as file:
   for line in file:
       print(line)

```

### How to Move the Cursor in a File

You can use the `seek()` method to move the file cursor to a specific position within the file. For example, `file.seek(0)` moves the cursor to the beginning of the file.

### How to Ensure a File is Closed After Using It

Using a `with` statement (context manager) automatically ensures that the file is closed when you're done with it. This is a recommended way to handle files, as it avoids the need to explicitly call `file.close()`.

## JSON (JavaScript Object Notation)

### What is JSON

JSON (JavaScript Object Notation) is a lightweight data interchange format. It is easy for humans to read and write and easy for machines to parse and generate. JSON is commonly used for data serialization and configuration files.

### What is Serialization

Serialization is the process of converting a data structure or object into a format that can be easily stored, transmitted, or reconstructed at a later time. In Python, the `json` module is often used for serialization.

### What is Deserialization

Deserialization is the process of reconstructing data from its serialized format. In Python, it involves taking a JSON string or other serialized data and converting it into a usable data structure or object.

### How to Convert a Python Data Structure to a JSON String

You can use the `json.dumps()` function to convert a Python data structure (e.g., a dictionary) to a JSON string.
```python
import json
data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)

```
### How to Convert a JSON String to a Python Data Structure

You can use the `json.loads()` function to convert a JSON string back into a Python data structure.
```python
import json
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)

```
