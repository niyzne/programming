# MakeUpperCase

---
## Info

Write a function which converts the input string to uppercase.

---
Fundamentals | Strings

---
## Code

Solution

```python
def make_upper_case(s):
    # Code here
```

Sample Tests

```python
import codewars_test as test
from solution import make_upper_case

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(make_upper_case("hello"), "HELLO")
```

---
## Code Solution

```python
def make_upper_case(s):
    return s.upper()
```

---