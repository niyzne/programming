# Reversed sequence

---
## Info

Build a function that returns an array of integers from n to 1 where `n>0`.

Example : `n=5` --> `[5,4,3,2,1]`

---
Fundamentals

---
## Code

Solution

```python
def reverse_seq(n):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import reverse_seq

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_seq(5),[5,4,3,2,1])
```

---
## Code Solution

```python
def reverse_seq(n):
    array = []
    for x in range(1, n+1):
        array.append(x)
    
    return array[::-1]
```

---
## Resources I used for help

https://www.w3schools.com/python/python_for_loops.asp

https://www.w3schools.com/python/python_dsa_lists.asp

https://www.digitalocean.com/community/tutorials/python-add-to-array

https://stackoverflow.com/questions/20774607/python-for-loop-inside-print

---