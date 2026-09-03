# Switch it Up!

---
## Info

When provided with a number between `0-9`, return it in words. Note that the input is guaranteed to be within the range of `0-9`.

Input: `1`

Output: `"One"`.

If your language supports it, try using a [switch statement](https://en.wikipedia.org/wiki/Switch_statement).

---
Fundamentals

---
## Code

Solution

```python
def switch_it_up(number):
    #your code here
    return ""
```

Sample Tests

```python
import codewars_test as test
from solution import switch_it_up

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(switch_it_up(0), "Zero")
        test.assert_equals(switch_it_up(9), "Nine")
```

---
## Code Solution

```python
def switch_it_up(num):
    if num == 0:
            return "Zero"
    elif num == 1:
            return "One"
    elif num == 2:
            return "Two"
    elif num == 3:
            return "Three"
    elif num == 4:
            return "Four"
    elif num == 5:
            return "Five"
    elif num == 6:
            return "Six"
    elif num == 7:
            return "Seven"
    elif num == 8:
            return "Eight"
    elif num == 9:
            return "Nine"
```

or

```python
def switch_it_up(n):
    words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
    return words[n]
```

---