# Sentence Smash

---
## Info

Sentence Smash

Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. **Be careful, there shouldn't be a space at the beginning or the end of the sentence!**

Example

```
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
```

Assumptions

- You can assume that you are only given words.
- You cannot assume the size of the array.
- You can assume that you do get an array.

What We're Testing

We're testing basic loops and string manipulation. This is for beginners who are just learning loops and string manipulation.

Disclaimer

This is for beginners so we want to test basic loops and string manipulation.

---
Strings | Arrays | Fundamentals

---
## Code

Solution

```python
def smash(words):
    return ""
```

Sample Tests

```python
import codewars_test as test
from solution import smash

@test.describe("smash")
def _():
    @test.it("Should return empty string for empty array.")
    def _():
        test.assert_equals(smash([]), "")
        
    @test.it("One word example should return the word.")
    def _():
        test.assert_equals(smash(["hello"]), "hello")
        
    @test.it("Multiple words should be separated by spaces.")
    def _():
        test.assert_equals(smash(["hello", "world"]), "hello world")
        test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
        test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")
```

---
## Code Solution

```python
def smash(words):
    return ' '.join(words)
```

or

```python
def smash(words):
    sentence = ' '.join(words)
    return sentence
```

---
## Resources I used for help

https://codepal.ai/code-generator/query/ybzCn3Sg/python-function-concatenate-array-words-into-sentence

https://blog.finxter.com/5-best-ways-to-convert-a-python-list-of-strings-to-a-single-string/

---