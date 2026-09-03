# Returning Strings

---
## Info

Create a function that accepts a parameter representing a `name` and returns the message: `"Hello, <name> how are you doing today?"`.

_[Make sure you type the exact thing I wrote or the program may not execute properly]_

---
Strings | Fundamentals

---
## Code

Solution

```python
def greet(name):
    #Good Luck (like you need it)
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import greet

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
        test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
```

---
## Code Solution

```python
def greet(name):
    return f'Hello, {name} how are you doing today?'
```

---