# If you can't sleep, just count sheep!!

---
## Info

If you can't sleep, just count sheeps!!
## Task:

Given a non-negative integer, `3` for example, return a string with a murmur: `"1 sheep...2 sheep...3 sheep..."`. Input will always be valid, i.e. no negative integers.

---
Fundamentals | Strings

---
## Code

Solution

```python
def count_sheep(n):
    # your code
```

Sample Tests

```python
import codewars_test as test
from solution import count_sheep

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_sheep(0), "");
        test.assert_equals(count_sheep(1), "1 sheep...");
        test.assert_equals(count_sheep(2), "1 sheep...2 sheep...")
        test.assert_equals(count_sheep(3), "1 sheep...2 sheep...3 sheep...")
```

---
## Code Solution

```python
def count_sheep(n):
    result = []
    for a in range(1, n+1):
        result.append(f'{a} sheep...')
    result_str = "".join(result)
    return result_str
```

---
## Resources I used for help

https://www.w3schools.com/python/ref_func_range.asp

https://pythonexamples.org/python-print-range-to-a-single-line-in-output/

https://www.geeksforgeeks.org/python/python-program-to-convert-a-list-to-string/

---