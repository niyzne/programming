# Convert a String to a Number!

---
## Info

Note: This kata is inspired by [Convert a Number to a String!](http://www.codewars.com/kata/convert-a-number-to-a-string/). Try that one too.

## Description

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

## Examples

```
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
```

---
Parsing | Strings | Fundamentals

---
## Code

Solution

```python
def string_to_number(s):
    # your code here
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import string_to_number

@test.describe("string_to_number")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_to_number("1234"), 1234)
        test.assert_equals(string_to_number("605"), 605)
        test.assert_equals(string_to_number("1405"), 1405)
        test.assert_equals(string_to_number("-7"), -7)

```

---
## Code Solution

```python
def string_to_number(s):
    return int(s)
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/convert-string-to-integer-in-python/

---