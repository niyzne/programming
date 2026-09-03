# Convert a Boolean to a String

---
## Info

Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

---
Strings | Fundamentals

---
## Code

Solution

```python
def boolean_to_string(b):
    #your code here
```

Sample Tests

```python
import codewars_test as test
from solution import boolean_to_string

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")
```

---
## Code Solution

```python
def boolean_to_string(b):
    if b:
        return 'True'
    return 'False'
```

---