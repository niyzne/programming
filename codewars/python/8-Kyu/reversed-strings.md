# Reversed Strings

---
## Info

Complete the solution so that it reverses the string passed into it.

```
'world'  =>  'dlrow'
'word'   =>  'drow'
```

---
Strings | Fundamentals

---
## Code

Solution

```python
def solution(string):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import solution

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution('world'), 'dlrow')
        test.assert_equals(solution('hello'), 'olleh')
        test.assert_equals(solution(''), '')
        test.assert_equals(solution('h'), 'h')
```

---
## Code Solution

```python
def solution(string):
    return string[::-1]
```

---
## Resources I used for help

https://www.w3schools.com/python/python_howto_reverse_string.asp

---