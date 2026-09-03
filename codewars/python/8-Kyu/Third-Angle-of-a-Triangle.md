# Third Angle of a Triangle

---
## Info

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

[https://en.wikipedia.org/wiki/Triangle](https://en.wikipedia.org/wiki/Triangle)

---
Fundamentals

---
## Code

Solution

```python
def other_angle(a, b):
    pass
```

Sample Tests

```python
import codewars_test as test

try:
    from solution import otherAngle as other_angle
except ImportError:
    from solution import other_angle

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(other_angle(30, 60), 90)
        test.assert_equals(other_angle(60, 60), 60)
        test.assert_equals(other_angle(43, 78), 59)
        test.assert_equals(other_angle(10, 20), 150)
```

---
## Code Solution

```python
def other_angle(a, b):
    return 180 - (a + b)
```

---