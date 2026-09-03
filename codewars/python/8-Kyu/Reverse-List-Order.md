# Reverse List Order

---
## Info

In this kata you will create a function that takes in a list and returns a list with the reverse order.

### Examples (Input -> Output)

```
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]
```

---
Lists | Fundamentals

---
## Code

Solution

```python
def reverse_list(l):
    'return a list with the reverse order of l'
```

Sample Tests

```python
import codewars_test as test
from solution import reverse_list

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_list([1,2,3,4]), [4,3,2,1])
        test.assert_equals(reverse_list([3,1,5,4]), [4,5,1,3])
        test.assert_equals(reverse_list([3,6,9,2]), [2,9,6,3])
        test.assert_equals(reverse_list([1]), [1])
```

---
## Code Solution

```python
def reverse_list(l):
    return list(reversed(l))
```

or

```python
def reverse_list(l):
    return l[::-1]
```

---