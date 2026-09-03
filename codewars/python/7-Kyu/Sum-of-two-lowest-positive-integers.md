# Sum of two lowest positive integers

---
## Info

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like `[19, 5, 42, 2, 77]`, the output should be `7`.

`[10, 343445353, 3453445, 3453545353453]` should return `3453455`.

---
Arrays | Fundamentals

---
## Code

Solution

```python
def sum_two_smallest_numbers(numbers):
    return 0
```

Sample Tests

```python
import codewars_test as test
from solution import sum_two_smallest_numbers


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])")
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]), 3453455)

    @test.it("sum_two_smallest_numbers([5, 8, 12, 18, 22])")
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)

    @test.it("sum_two_smallest_numbers([7, 15, 12, 18, 22])")
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)

    @test.it("sum_two_smallest_numbers([25, 42, 12, 18, 22])")
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
```

---
## Code Solution

```python
def sum_two_smallest_numbers(nums):
    new_list = []
    for digit in nums:
        if digit > 0:
            new_list.append(digit)
    
    sorted_list = sorted(new_list)
    return sorted_list[0] + sorted_list[1]
```

realized afterwards there aren't any negative numbers either way

```python
def sum_two_smallest_numbers(nums):
    return sum(sorted(nums)[:2])
```

---
## Resources I used for help

https://stackoverflow.com/questions/76328254/how-can-i-extract-two-values-from-a-list-of-lists-in-python-where-the-sublist-b

https://www.geeksforgeeks.org/dsa/to-find-smallest-and-second-smallest-element-in-an-array/

https://www.geeksforgeeks.org/python/python-remove-negative-elements-in-list/

https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-213.php

---