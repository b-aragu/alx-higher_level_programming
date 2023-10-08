# Understanding Testing in Python: `doctest` and `unittest`

## Introduction

Testing is a crucial aspect of software development. It helps ensure that your code works as expected and prevents regressions when you make changes. In Python, there are two primary testing libraries: `doctest` and `unittest`. This README will provide an introduction to both, along with examples to help you get started.

## 1. `doctest`

### What is `doctest`?

`doctest` is a lightweight testing framework that allows you to embed test cases within your Python docstrings. It's a simple and convenient way to ensure that your code examples in documentation are accurate and that your functions behave as intended.

### How to Use `doctest`

1. Import the `doctest` module:
```
import doctest
```
1. Write your test cases in docstrings using the `>>>` prompt.
2. Run the tests using `doctest.testmod()`.

### Example

Let's say you have a function `add`:
```
def add(a, b):
    """
    This function adds two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

```
- To run the doctest 
```
if __name__ == "__main__":
    doctest.testmod()

```

### Running `doctest`

Save the code in a Python file (e.g., `my_module.py`) and run it. If everything is correct, there will be no output. If there's an issue, `doctest` will print an error message.
you can also use `python3 -m doctest my_module.py -v` to run it on the command line

## 2. `unittest`

### What is `unittest`?

`unittest` is a more comprehensive testing framework that provides more features for writing and organizing test cases. It's suitable for larger projects and offers more advanced testing capabilities.
### How to Use `unittest`

1. Import the `unittest` module:
	```
	import unitest
	```
2.  Create a test class that inherits from `unittest.TestCase`.
  
3. Write test methods within the test class. Test method names should start with `test_`.
    
4. Use `assert` statements to check if the code behaves as expected.
    
5. Run the tests using the `unittest` test runner.
    

### Example

Let's say you have a `Calculator` class:
```
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

```

To create taste case for it 
```
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()

```
### Running `unittest`

Save the code in a Python file (e.g., `test_calculator.py`) and run it. `unittest` will discover and execute the test cases, and you'll see output indicating whether the tests passed or failed.

## Conclusion

Both `doctest` and `unittest` are valuable tools for testing your Python code. `doctest` is simple and fits well with docstrings, while `unittest` offers more advanced features for larger projects. Choose the one that best suits your needs, and remember that testing is essential for writing reliable and maintainable code.
