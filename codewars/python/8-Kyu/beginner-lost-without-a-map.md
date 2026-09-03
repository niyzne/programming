# Beginner - Lost Without a Map

---
## Info

Given an array of integers, return a new array with each value doubled.

For example:

`[1, 2, 3] --> [2, 4, 6]`

---
Arrays | Fundamentals

---
## Code

Solution

```python
def maps(a):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import maps

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
        test.assert_equals(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        test.assert_equals(maps([]), [])
```

---
## Code Solution

```python
def maps(a):
	return [b * 2 for b in a]
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/python-double-each-list-element/

---
