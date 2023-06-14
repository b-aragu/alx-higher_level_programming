- open() returns a file object
`open(filename, mode, encoding=None)`
`filename` ~ the name of the file e.g. file.txt
`mode` - can either be read 'r', write 'w', append 'a', adding 'b' to the modes open file in binary mode
- with keyword is used to explicitly manage resources that needs to be opened and closed e.g files
The general syntax is `with expression as target`
```
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
- `f.tell()` returns an integer giving the objects current position in the file rep as number of bytes from begining of file when in binary mode and an  opaque number when in text mode
- To change file position use `f.seek(offset, whence)`

### Saving Structured data with _json_
- Javascript object notation is a popular data interchange format
- To save structured data using JSON, you can follow these general steps:
1. Prepare your data in a structured format, such as a dictionary or a list of dictionaries, in your programming language of choice. Ensure that the data is compatible with JSON data types (strings, numbers, booleans, lists, dictionaries).
    
2. Import the JSON library or module provided by your programming language. For example, in Python, you can import the `json` module.
    
3. Use the appropriate function or method provided by the JSON library to convert your data into a JSON string. In Python's `json` module, you can use the `json.dumps()` function to serialize the data.
    
4. Open a file for writing in your preferred mode (e.g., "w" for writing) using the built-in file handling functions or classes provided by your programming language.
5. Write the JSON string to the file using the file handling functions or methods. In Python, you can use the `write()` method of the file object.
6. Close the file to ensure that the changes are saved properly.

e.g. 
```
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
