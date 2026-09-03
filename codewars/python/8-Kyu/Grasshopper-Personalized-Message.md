# Grasshopper - Personalized Message

---
## Info

Create a function that gives a personalized greeting. This function takes two parameters: `name` and `owner`.

Use conditionals to return the proper message:

|case|return|
|---|---|
|name equals owner|'Hello boss'|
|otherwise|'Hello guest'|

---
Fundamentals | Strings

---
## Code

Solution

```python
def greet(name, owner):
    # Add code here
```

Sample Tests

```python
import codewars_test as test
from solution import greet

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
        test.assert_equals(greet('Greg', 'Daniel'), 'Hello guest')
```

---
## Code Solution

```python
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    return 'Hello guest'
```

---