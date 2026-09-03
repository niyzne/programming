# Square(n) Sum

---
## Info

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for `[1, 2, 2]` it should return `9` because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.

---
Arrays | Lists | Fundamentals

---
## Code

Solution

```python
def square_sum(numbers):
    #your code here
```

Sample Tests

```python
import codewars_test as test
from solution import square_sum

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_sum([1,2]), 5)
        test.assert_equals(square_sum([0, 3, 4, 5]), 50)
        test.assert_equals(square_sum([]), 0)
        test.assert_equals(square_sum([-1,-2]), 5)
        test.assert_equals(square_sum([-1,0,1]), 2)
```

---
## Code Solution

```python
def square_sum(numbers):
    return sum([n ** 2 for n in numbers])
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/python-program-to-find-sum-of-array/

https://www.geeksforgeeks.org/python/numpy-square-python/

https://www.geeksforgeeks.org/python/find-average-list-python/

https://www.geeksforgeeks.org/python/python-program-to-find-sum-of-array/

---