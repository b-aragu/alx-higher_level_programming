## Guide to Doctests in Python

### What are Doctests?

Doctests are a way to include tests within your Python documentation. They are written as part of docstrings and can serve both as documentation and executable tests. Doctests help ensure that your code examples in the documentation are accurate and up-to-date.

### Writing a Simple Doctest

Here's a basic example of a doctest within a docstring:

```python
def add_numbers(a, b):
    """
    This function adds two numbers.

    >>> add_numbers(2, 3)
    5

    >>> add_numbers(-1, 1)
    0
    """
    return a + b
```

In this example, the docstring includes examples of how to use the `add_numbers` function along with their expected outputs.

### Running Doctests

To run doctests, you can use the `doctest` module that comes with Python. Save the above code in a file (e.g., `math_operations.py`) and run the following command:

```bash
python -m doctest math_operations.py
```

Replace `math_operations.py` with the actual filename.

### Guidelines for Writing Doctests

1. **Use Realistic Examples:**
   - Provide examples that users might encounter in real scenarios.

2. **Include Both Inputs and Outputs:**
   - Include both input values and the expected output in your doctests.

3. **Keep it Concise:**
   - Doctests are meant to be concise examples. Avoid complex scenarios that might make the documentation less readable.

4. **Update Doctests as Code Changes:**
   - If you make changes to your code, remember to update the corresponding doctests to reflect those changes.

5. **Use Expressive Docstrings:**
   - Write clear and expressive docstrings that serve as both documentation and test cases.

### Doctests in Classes

Doctests can also be used in class docstrings:

```python
class Calculator:
    """
    A simple calculator class.

    >>> calc = Calculator()
    >>> calc.add(2, 3)
    5

    >>> calc.subtract(5, 3)
    2
    """
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
```

### Doctests in Modules

Doctests can be included at the module level:

```python
# math_operations.py

"""
A module for basic math operations.

>>> add_numbers(2, 3)
5

>>> subtract_numbers(5, 3)
2
"""

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b
```

### Conclusion

Doctests are a powerful tool for ensuring that your code examples in the documentation remain accurate and executable. By following the guidelines and examples provided, you can leverage doctests to improve the reliability and clarity of your Python documentation.
