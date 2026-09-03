# Sum Arrays

---
## Info

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return `0`.

Examples

Input: `[1, 5.2, 4, 0, -1]`  
Output: `9.2`

Input: `[-2.398]`  
Output: `-2.398`

Input: `[]`  
Output: `0`

Assumptions

- You can assume that you are given a (possibly empty) valid array containing only numbers.

What We're Testing

We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.  
Advanced users may find this extremely easy and can easily write this in one line.

---
Arrays | Fundamentals

---
## Code

Solution

```python
def sum_array(a):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import sum_array

@test.describe("Testing sum array")
def tests():
    @test.it("Fixed tests")
    def fixed_tests(): 
        test.assert_equals(sum_array([]), 0)
        test.assert_equals(sum_array([1, 2, 3]), 6)
        test.assert_equals(sum_array([1.1, 2.2, 3.3]), 6.6)
        test.assert_equals(sum_array([4, 5, 6]), 15)
        test.assert_equals(sum_array(range(101)), 5050)
```

---
## Code Solution

```python
def sum_array(a):
    return sum(a)
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/python-program-to-find-sum-of-array/

---
