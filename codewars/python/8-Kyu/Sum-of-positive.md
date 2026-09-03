# Sum of positive

---
## Info

### Task

You get an array of numbers, return the sum of all of the positives ones.

### Example

- `[1, -4, 7, 12]` => 1+7+12=20 1 + 7 + 12 = 20 1+7+12=20

### Note

If there is nothing to sum, the sum is default to `0`.

---
Arrays | Fundamentals

---
## Code

Solution

```python
def positive_sum(arr):
    # Your code here
    return 0
```

Sample Tests

```python
import codewars_test as test
from solution import positive_sum

@test.describe("positive_sum")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(positive_sum([1,2,3,4,5]),15)
        test.assert_equals(positive_sum([1,-2,3,4,5]),13)
        test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
        
    @test.it("returns 0 when array is empty")
    def empty_case():
        test.assert_equals(positive_sum([]),0)      
        
    @test.it("returns 0 when all elements are negative")
    def negative_case():
        test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)
```

---
## Code Solution

```python
def positive_sum(arr):
    total = 0 
    for num in arr:
        if num > 0:
            total += num
    return total
```

---
## Resources I used for help

https://stackoverflow.com/questions/28798812/compute-the-sum-of-the-positive-numbers-in-a-list-in-python

---