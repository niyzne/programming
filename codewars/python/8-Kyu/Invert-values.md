# Invert values

---
## Info

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
```

---
Lists | Fundamentals | Arrays

---
## Code

Solution

```python
def invert(lst):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import invert

@test.describe("Invert values")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        test.assert_equals(invert([]), [])
```

---
## Code Solution

```python
def invert(lst):
    newlist = []
    for i in lst:
        newlist.append(-i)
    return newlist
```

---
## Resources I used for help

https://www.w3schools.com/python/ref_list_append.asp

https://www.geeksforgeeks.org/python/how-to-modify-a-list-while-iterating-in-python/

---