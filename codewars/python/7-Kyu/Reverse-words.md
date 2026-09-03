# Reverse words

---
## Info

Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.

Examples

```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

---
Strings | Fundamentals

---
## Code

Solution

```python
def reverse_words(text):
    pass #go for it
```

Sample Tests

```python
import codewars_test as test
from solution import reverse_words

@test.describe("Sample Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god', "Input: 'The quick brown fox jumps over the lazy dog.'")
        test.assert_equals(reverse_words('apple'), 'elppa', "Input: 'apple'")
        test.assert_equals(reverse_words('a b c d'), 'a b c d', "Input: 'a b c d'")
        test.assert_equals(reverse_words('  double  spaced  words  '), '  elbuod  decaps  sdrow  ', "Input: '  double  spaced  words  '")
```

---
## Code Solution

```python
def reverse_words(text):
    words = text.split(" ")

    a = []
    for word in words:
        a.append(word[::-1])
    
    return " ".join(a)
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/python-reverse-word-sentence/

https://www.geeksforgeeks.org/python/convert-string-to-integer-in-python/

---