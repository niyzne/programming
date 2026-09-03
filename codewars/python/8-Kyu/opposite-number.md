# Opposite number

---
## Info

Very simple, given a number, find its opposite (additive inverse).

Examples:

```
1: -1
14: -14
-34: 34
```
---
Fundamentals

---
## Code

Solution

```python
def opposite(number):
  # your solution here
```

Sample Tests

```python
import codewars_test as test
from solution import opposite

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(opposite(1),-1)
        test.assert_equals(opposite(25.6), -25.6)
        test.assert_equals(opposite(0), 0)
        test.assert_equals(opposite(1425.2222), -1425.2222)
        test.assert_equals(opposite(-3.1458), 3.1458)
        test.assert_equals(opposite(-95858588225),95858588225)
    
```

---
## Code Solution

```python
def opposite(number):
  return number * -1
```

---
