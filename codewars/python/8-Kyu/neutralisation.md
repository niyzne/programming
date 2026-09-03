# Neutralisation

---
## Info

Given two strings comprised of `+` and `-`, return a new string which shows how the two strings interact in the following way:

- When positives and positives interact, they _remain positive_.
- When negatives and negatives interact, they _remain negative_.
- But when negatives and positives interact, they _become neutral_, and are shown as the number `0`.

Worked Example

```
("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
```

Examples

```
("--++--", "++--++") ➞ "000000"

("-+-+-+", "-+-+-+") ➞ "-+-+-+"

("-++-", "-+-+") ➞ "-+00"
```

Notes

The two strings will be the same length.

---
Algorithms | Strings

---
## Code

Solution

```python
def neutralise(s1, s2):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import neutralise

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(neutralise("--++--", "++--++"), "000000")
        test.assert_equals(neutralise("-+-+-+", "-+-+-+"), "-+-+-+")
        test.assert_equals(neutralise("-++-", "-+-+"), "-+00")
        test.assert_equals(neutralise("--++", "++++"), "00++")
        test.assert_equals(neutralise("+++--+---", "++----++-"), "++0--000-")
        test.assert_equals(neutralise("-----", "-----"), "-----")
        test.assert_equals(neutralise("-+", "++"), "0+")
        test.assert_equals(neutralise("--", "-+"), "-0")
        test.assert_equals(neutralise("-++", "+--"), "000")
        test.assert_equals(neutralise("++-++--++-", "-+++-++-++"), "0+0+0000+0")
        test.assert_equals(neutralise("-++-+-++-", "+-++++---"), "00+0+000-")
        test.assert_equals(neutralise("---++-+--", "-+++--++-"), "-00+0-+0-")
        test.assert_equals(neutralise("+-----+++-", "--+-+-++--"), "0-0-0-++0-")
        test.assert_equals(neutralise("+-----+-", "---++-++"), "0--00-+0")
        test.assert_equals(neutralise("-+--+-+---", "-+--+-+-+-"), "-+--+-+-0-")
        test.assert_equals(neutralise("+-+", "-++"), "00+")
        test.assert_equals(neutralise("-++", "-+-"), "-+0")
        test.assert_equals(neutralise("---+", "-+++"), "-00+")
        test.assert_equals(neutralise("+--", "+--"), "+--")
        test.assert_equals(neutralise("--+++-+-", "+++++---"), "00+++-0-")
```

---
## Code Solution

```python
def neutralise(s1, s2):
    result = ''
    for a, b in zip(s1, s2):
        if a == '+' and b == '+':
            result += '+'
        elif a == '-' and b == '-':
            result += '-'
        else:
            result += '0'
    return result
```

---
