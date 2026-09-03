# Descending Order

---
## Info

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

### Examples:

Input: `42145` Output: `54421`

Input: `145263` Output: `654321`

Input: `123456789` Output: `987654321`

---
Fundamentals

---
## Code

Solution

```python
def descending_order(num):
    # Bust a move right here
```

Sample Tests

```python
import codewars_test as test

try:
    from solution import Descending_Order as descending_order
except ImportError:
    from solution import descending_order

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(descending_order(0), 0)
        test.assert_equals(descending_order(15), 51)
        test.assert_equals(descending_order(123456789), 987654321)
```

---
## Code Solution

```python
def descending_order(n):
    return int(''.join(sorted(str(n))[::-1]))
```

---
## Resources I used for help

https://realpython.com/python-sort/

https://www.geeksforgeeks.org/python/python-convert-number-to-list-of-integers/

https://www.geeksforgeeks.org/python/python-reversing-list/

https://www.geeksforgeeks.org/python/python-converting-all-strings-in-list-to-integers/

https://www.pythonhelp.org/tutorials/convert-list-to-int/

---