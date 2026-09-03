# Remove First and Last Character

---
# Remove First and Last Character

## Task

Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.

**Important:** Your function should handle strings of any `length ≥ 2` characters. For strings with exactly `2` characters, return an empty string.
## Examples

```
'eloquent' --> 'loquen'
'country'  --> 'ountr' 
'person'   --> 'erso'
'ab'       --> '' (empty string)
'xyz'      --> 'y'
```
## Requirements

- The input string will always have at least 2 characters
- For strings with exactly 2 characters, return an empty string
- For strings with 3 or more characters, remove the first and last character
- The function should handle strings containing letters, numbers, and special characters
## Test Cases

Your solution will be tested against:

- Basic functionality with common words
- Edge cases with 2-character and 3-character strings
- Strings containing numbers and special characters
- Random test cases of varying lengths

---
Strings | Fundamentals

---
## Code

Solution

```R
removeChar <- function(str){
    # your code here
}
```

Sample Tests

```R
test_that('basic tests', {
  expect_equal(removeChar('eloquent'), 'loquen')
  expect_equal(removeChar('country'), 'ountr')
  expect_equal(removeChar('person'), 'erso')
  expect_equal(removeChar('place'), 'lac')
  expect_equal(removeChar('ok'), '')
})
```

---
## Code Solution

```R
removeChar <- function(str){ gsub('^.|.$', '', str) }
```

---
## Resources I used for help

https://stackoverflow.com/questions/35113553/r-remove-first-character-from-string

---