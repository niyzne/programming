# Remove exclamation marks

---
## Info

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

---
Fundamentals | Strings

---
## Code

Solution

```R
remove_exclamation_marks <- function(s){
  
}
```

Sample Tests

```R
test_that('Basic tests', {
  expect_equal(remove_exclamation_marks("Hello World!"), "Hello World")
  expect_equal(remove_exclamation_marks("Hello World!!!"), "Hello World")
  expect_equal(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
  expect_equal(remove_exclamation_marks(""), "")
  expect_equal(remove_exclamation_marks("Oh, no!!!"), "Oh, no")
})
```

---
## Code Solution

```R
remove_exclamation_marks <- function(s){ 
  gsub('!', '', s)
}
```

---
## Resources I used for help

https://www.statology.org/r-remove-character-from-string/

---