# Isograms

---
## Info

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**Example: (Input --> Output)**

```
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
```

---
Strings | Fundamentals

---
## Code

Solution

```python
def is_isogram(string):
    #your code here
```

Sample Tests

```python
import codewars_test as test
from solution import is_isogram

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():      
        test.assert_equals(is_isogram("Dermatoglyphics"), True )
        test.assert_equals(is_isogram("isogram"), True )
        test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
        test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
        test.assert_equals(is_isogram("isIsogram"), False )
        test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )
```

---
## Code Solution

```python
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)
```

---
## Resources I used for help

https://medium.com/@pythonchallengers/python-challenge-check-if-a-string-is-an-isogram-8e6eb7bdca43

https://stackoverflow.com/questions/41870749/determining-if-a-string-is-an-isogram

---