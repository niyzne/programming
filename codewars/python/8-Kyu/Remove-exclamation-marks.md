# Remove exclamation marks

---
## Info

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

---
Fundamentals | Strings

---
## Code

Solution

```python
def remove_exclamation_marks(s):
    #your code here
```

Sample Tests

```python
import codewars_test as test
from solution import remove_exclamation_marks

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_exclamation_marks("Hello World!"), "Hello World")
        test.assert_equals(remove_exclamation_marks("Hello World!!!"), "Hello World")
        test.assert_equals(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
        test.assert_equals(remove_exclamation_marks(""), "")
        test.assert_equals(remove_exclamation_marks("Oh, no!!!"), "Oh, no")
```

---
## Code Solution

```python
def remove_exclamation_marks(s):
    return s.replace("!", "")
```

---
## Resources I used for help

https://builtin.com/software-engineering-perspectives/python-remove-character-from-string

---