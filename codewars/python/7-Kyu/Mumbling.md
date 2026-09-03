# Mumbling

---
## Info

This time no story, no theory. The examples below show you how to write function `accum`:

#### Examples:

```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```

The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.

---
Fundamentals | Strings | Puzzles

---
## Code

Solution

```python
def accum(st):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import accum

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        test.assert_equals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        test.assert_equals(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
        test.assert_equals(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
        test.assert_equals(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
```

---
## Code Solution

```python
def accum(st):
    lists = []
    for i in range(len(st)):
        lists.append(((st.lower()[i]) * (i + 1)).title())

    return "-".join(lists)
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/how-to-access-index-in-for-loop-python/

https://www.geeksforgeeks.org/python/python-program-convert-string-list/

https://www.geeksforgeeks.org/python/how-to-split-lists-in-python/

https://www.geeksforgeeks.org/python/python-program-to-convert-a-list-to-string/

---