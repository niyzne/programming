# Century From Year

---
## Info

Introduction

The first century spans from the **year 1** up to _and including_ the year 100, the second century - from the year 101 up to _and including_ the year 200, etc.

Task

Given a year, return the century it is in.

Examples

```
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
```

Note: this kata uses strict construction as shown in the description and the examples, you can read more about it [here](https://en.wikipedia.org/wiki/Century)

---
Fundamentals | Mathematics

---
## Code

Solution

```python
def century(year):
    # Finish this :)
    return
```

Sample Tests

```python
import codewars_test as test
from solution import century

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(century(1705), 18, 'Testing for year 1705')
        test.assert_equals(century(1900), 19, 'Testing for year 1900')
        test.assert_equals(century(1601), 17, 'Testing for year 1601')
        test.assert_equals(century(2000), 20, 'Testing for year 2000')
        test.assert_equals(century(356), 4, 'Testing for year 356')
        test.assert_equals(century(89), 1, 'Testing for year 89')
```

---
## Code Solution

```python
def century(year):
    century = (year - 1) // 100 + 1
    return century
```

---
## Resources I used for help

https://stackoverflow.com/questions/46356820/year-to-century-function

---
