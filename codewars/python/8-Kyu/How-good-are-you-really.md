# How good are you really?

---
## Info

There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return `true` if you're better, else `false`!

### Note:

Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

---
Fundamentals

---
## Code

Solution

```python
def better_than_average(class_points, your_points):
    # Your code here
```

Sample Tests

```python
import codewars_test as test

def test_it(arr, points, expected):
    @test.it(f"Testing with arr={arr}, points={points}")
    def _():
        test.assert_equals(better_than_average(arr, points), expected, f"better_than_average({arr}, {points}) should return {expected}")

@test.describe("Basic Tests")
def basic_tests():
    test_it([2, 3], 5, True)
    test_it([100, 40, 34, 57, 29, 72, 57, 88], 75, True)
    test_it([12, 23, 34, 45, 56, 67, 78, 89, 90], 69, True)
    test_it([41, 75, 72, 56, 80, 82, 81, 33], 50, False)
    test_it([29, 55, 74, 60, 11, 90, 67, 28], 21, False)
    test_it([100, 90, 80], 85, False)
    test_it([50, 50, 50], 50, False)
```

---
## Code Solution

```python
def better_than_average(class_points, your_points):
    class_avg = sum(class_points) / len(class_points)
    if your_points > class_avg:
        return True
    return False
```

or

```python
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/find-average-list-python/

https://www.geeksforgeeks.org/python/python-program-to-find-sum-of-array/

---