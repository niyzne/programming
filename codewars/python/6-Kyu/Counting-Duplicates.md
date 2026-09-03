# Counting Duplicates

---
## Info

Count the number of Duplicates

Write a function that will return the count of **distinct case-insensitive** alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example

"abcde" -> 0 `# no characters repeats more than once`  
"aabbcde" -> 2 `# 'a' and 'b'`  
"aabBcde" -> 2 ``# 'a' occurs twice and 'b' twice (`b` and `B`)``  
"indivisibility" -> 1 `# 'i' occurs six times`  
"Indivisibilities" -> 2 `# 'i' occurs seven times and 's' occurs twice`  
"aA11" -> 2 `# 'a' and '1'`  
"ABBA" -> 2 `# 'A' and 'B' each occur twice`

---
Strings | Fundamentals

---
## Code

Solution

```python
def duplicate_count(text):
    # Your code goes here
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import duplicate_count

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""),        0, 'duplicate_count("")'       )
        test.assert_equals(duplicate_count("abcde"),   0, 'duplicate_count("abcde")'  )
        test.assert_equals(duplicate_count("abcdeaa"), 1, 'duplicate_count("abcdeaa")')
        test.assert_equals(duplicate_count("abcdeaB"), 2, 'duplicate_count("abcdeaB")')
        
        test.assert_equals(duplicate_count("Indivisibilities"), 2, 'duplicate_count("Indivisibilities")')

```

---
## Code Solution

```python
def duplicate_count(texts):
    text = texts.lower()
    
    seen = {}
    for char in text:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] = seen[char] + 1
    
    result = 0
    for value in seen.values():
        if value >= 2:
            result += 1
        
    return result
```

---
## Resources I used for help

https://stackoverflow.com/questions/7002429/how-to-extract-all-values-from-a-dictionary-in-python

https://www.w3schools.com/python/python_dictionaries_access.asp

https://stackoverflow.com/questions/48371856/count-the-number-of-occurrences-of-a-certain-value-in-a-dictionary-in-python

https://www.geeksforgeeks.org/python/python-count-dictionary-items/

https://www.geeksforgeeks.org/python/counting-the-frequencies-in-a-list-using-dictionary-in-python/

https://www.geeksforgeeks.org/python/iterate-over-characters-of-a-string-in-python/

https://realpython.com/python-counter/

https://www.pythonmorsels.com/using-counter/

---
