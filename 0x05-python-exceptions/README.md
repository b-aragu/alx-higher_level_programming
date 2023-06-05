## Python errors and exceptions
---------
- Errors in python may occur in two ways
1. Syntax errors
2. Logical errors
---------
### 1. Syntax errors
- The occur when the language rules are not followed correctly.
e.g missing parentheses punctuation marks e.t.c
### 2. Logical errors
- They occur when the code runs but not as expected

## Exceptions
- These are errors detected during execution
- They include:
1. `SyntaxError`: Raised when the code violates the syntax rules of Python. It usually occurs due to missing parentheses, incorrect indentation, or misspelled keywords.

2. `NameError`: Raised when a local or global name is not found. This typically happens when a variable or function is referenced before it is defined or outside of its scope.

3. `TypeError`: Raised when an operation or function is applied to an object of an inappropriate type. For example, trying to perform arithmetic operations on incompatible data types like adding a string to an integer.

4. `IndexError`: Raised when trying to access a sequence (such as a list or string) using an invalid index. It occurs when the index is out of range, i.e., less than 0 or greater than the length of the sequence.

5. `ValueError`: Raised when a function receives an argument of the correct type but an inappropriate value. For instance, passing an invalid argument to a built-in function or trying to convert a string to an integer when it contains non-numeric characters.

6. `KeyError`: Raised when a dictionary key is not found. It occurs when trying to access a key that doesn't exist in the dictionary.

7. `FileNotFoundError`: Raised when attempting to open or manipulate a file that does not exist.

8. `ZeroDivisionError`: Raised when dividing a number by zero. This error occurs due to an invalid arithmetic operation.

9. `AttributeError`: Raised when an attribute reference or assignment fails. It typically occurs when trying to access an attribute or method that does not exist for a given object.

10. `ImportError`: Raised when an import statement fails to find the specified module or package.

