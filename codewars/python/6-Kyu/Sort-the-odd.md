# Sort the odd

---
## Info

## Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

### Examples

```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

---
Fundamentals | Arrays | Sorting

---
## Code

Solution

```python
def sort_array(source_array):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import sort_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        test.assert_equals(sort_array([]),[])
        test.assert_equals(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
        test.assert_equals(sort_array([2, 22, 37, 11, 4, 1, 5, 0]), [2, 22, 1, 5, 4, 11, 37, 0])
        test.assert_equals(sort_array([1, 111, 11, 11, 2, 1, 5, 0]),[1, 1, 5, 11, 2, 11, 111, 0])
        test.assert_equals(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        test.assert_equals(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]),[0, 1, 2, 3, 4, 5, 8, 7, 6, 9])
```

---
## Code Solution

```python
def sort_array(source_array):
    new_array = []
    
    for n in source_array:
        if n % 2 != 0:
            new_array.append(n)
    
    odds = sorted(new_array)

    result = []
    i = 0
    
    for x in source_array:
        if x % 2 == 0:
            result.append(x)
        else:
            result.append(odds[i])
            i += 1

    return result
```

---
## Resources I used for help

https://stackoverflow.com/questions/44461172/sort-the-odd-numbers-in-the-list

---