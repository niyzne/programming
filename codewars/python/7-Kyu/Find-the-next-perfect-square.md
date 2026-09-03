# Find the next perfect square!

---
## Info

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the `findNextSquare` method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either `-1` or an empty value like `None` or `null`, depending on your language. You may assume the argument is non-negative.
## Examples ( Input --> Output )

```
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
```

---
Algebra | Fundamentals

---
## Code

Solution

```python
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1
```

Sample Tests

```python
import codewars_test as test
from solution import find_next_square

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should return the next square for perfect squares")
    def basic_test_cases():
        test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
        test.assert_equals(find_next_square(625), 676, "Wrong output for 625")
        test.assert_equals(find_next_square(319225), 320356, "Wrong output for 319225")
        test.assert_equals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")

    @test.it("should return -1 for numbers which aren't perfect squares")
    def _():
        test.assert_equals(find_next_square(155), -1, "Wrong output for 155")
        test.assert_equals(find_next_square(342786627), -1, "Wrong output for 342786627")
```

---
## Code Solution

```python
import math

def find_next_square(sq):
    
    root = math.sqrt(sq)
    
    if root.is_integer():
        return (root + 1) ** 2
    return -1
```

---
## Resources I used for help

https://www.geeksforgeeks.org/maths/perfect-squares/

https://docs.python.org/3/library/math.html

https://www.geeksforgeeks.org/python/python-if-else/

---