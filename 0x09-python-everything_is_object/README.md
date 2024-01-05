# 0x09. Python - Everything is object
----
# Lists

## List Basics
A list is an ordered collection of values, each identified by an index. The elements of a list can be of any type, and lists are considered sequences, similar to strings.

### Creating Lists
You can create a new list by enclosing its elements in square brackets:
```python
numbers = [10, 20, 30, 40]
words = ["spam", "bungee", "swallow"]
mixed_list = ["hello", 2.0, 5, [10, 20]]
empty_list = []
```

### List Assignment
Lists can be assigned to variables, passed as function parameters, and used in various contexts:
```python
vocabulary = ["ameliorate", "castigate", "defenestrate"]
numbers = [17, 123]
empty = []
```

## Accessing Elements
You can access elements of a list using the bracket operator (`[]`). Indices start at 0, and negative indices count from the end:
```python
print(numbers[0])  # Output: 17
print(numbers[-1])  # Output: 123
```

## List Length
The `len` function returns the length of a list, useful for loop bounds:
```python
horsemen = ["war", "famine", "pestilence", "death"]
num = len(horsemen)
for i in range(num):
    print(horsemen[i])
```

## List Membership
The `in` operator checks if an element is in a list:
```python
print("pestilence" in horsemen)  # Output: True
print("debauchery" not in horsemen)  # Output: True
```

## List Operations
Lists support concatenation and repetition:
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # Concatenation
print(c)  # Output: [1, 2, 3, 4, 5, 6]

d = [0] * 4  # Repetition
print(d)  # Output: [0, 0, 0, 0]
```

## List Slices
List slices allow you to extract sublists:
```python
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])  # Output: ['b', 'c']
```

## The `range` Function
`range` generates lists of consecutive integers:
```python
print(range(1, 5))  # Output: [1, 2, 3, 4]
print(range(10))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Lists are Mutable
Lists can be modified by assignment:
```python
fruit = ["banana", "apple", "quince"]
fruit[0] = "pear"
fruit[-1] = "orange"
```

## List Deletion
The `del` statement removes elements from a list:
```python
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
del a_list[1:5]
print(a_list)  # Output: ['a', 'f']
```

## Objects and Values
Variables refer to objects, and `==` checks values, while `is` checks object identity:
```python
a = "banana"
b = "banana"
print(a == b)  # Output: True
print(a is b)  # Output: True
```

## Aliasing
Assigning one variable to another creates aliases, leading to shared changes:
```python
a = [1, 2, 3]
b = a
b[0] = 5
print(a)  # Output: [5, 2, 3]
```

## Cloning Lists
Use the slice operator to create a new list (clone) with the same elements:
```python
a = [1, 2, 3]
b = a[:]
print(b)  # Output: [1, 2, 3]
```

## Nested Lists
Lists can contain other lists (nested lists):
```python
nested = ["hello", 2.0, 5, [10, 20]]
print(nested[3][1])  # Output: 20
```

## Matrices
Nested lists are often used to represent matrices:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])  # Output: 5
```

## Lists and For Loops
For loops work seamlessly with lists:
```python
for horseman in horsemen:
    print(h)

-------

Test Driven Development

-------
Test-driven development (TDD) is a software development methodology involving iterative steps guided by automated tests. In TDD, tests are written first, expressing incremental refinements of the desired feature. The `doctest` module in Python facilitates TDD by allowing tests to be embedded in docstrings.

For example, consider creating a function `make_matrix(rows, columns)` to generate a matrix. The initial test:

```python
def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    """
```

Running the test using `doctest.testmod()` reveals a failure due to the function not returning the expected matrix. Following the TDD principle of implementing the simplest solution to pass the test, an initial implementation is provided:

```python
def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    """
    return [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

While this passes the test, the implementation is flawed as it always returns the same matrix. To address this, a more general solution is motivated by adding a new test:

```python
def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      >>> make_matrix(4, 2)
      [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

This leads to a failing test, highlighting the need for a more flexible solution. A new implementation using a list comprehension is provided:

```python
def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      >>> make_matrix(4, 2)
      [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0] * columns for _ in range(rows)]
```

This solution appears correct, but a subsequent bug is discovered when modifying elements of the matrix. The issue arises from the fact that each row is an alias of the others. To address this, a failing test is added:

```python
def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      >>> make_matrix(4, 2)
      [[0, 0], [0, 0], [0, 0], [0, 0]]
      >>> m = make_matrix(4, 2)
      >>> m[1][1] = 7
      >>> m
      [[0, 0], [0, 7], [0, 0], [0, 0]]
    """
    return [[0] * columns for _ in range(rows)]
```

This failure motivates the development of a better solution, resulting in a more robust and correct implementation:

```python
def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      >>> make_matrix(4, 2)
      [[0, 0], [0, 0], [0, 0], [0, 0]]
      >>> m = make_matrix(4, 2)
      >>> m[1][1] = 7
      >>> m
      [[0, 0], [0, 7], [0, 0], [0, 0]]
    """
    matrix = []
    for row in range(rows):
        matrix += [[0] * columns]
    return matrix
```

In summary, TDD guides the development process by enforcing the creation of tests before code, promoting a step-by-step approach to problem-solving, and ensuring a robust and well-tested codebase.

