# Even or Odd

---
## Info

Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Mathematics | Fundamentals

---
## Code

Solution

```R
even_or_odd <- function(n) {
  # your code here
}
```

Sample Tests

```R
test_that('even_or_odd(1) returns "Odd"', {
  expect_equal(even_or_odd(1), "Odd")
})

test_that('even_or_odd(2) returns "Even"', {
  expect_equal(even_or_odd(2), "Even")
})

test_that('even_or_odd(0) returns "Even"', {
  expect_equal(even_or_odd(0), "Even")
})

test_that('even_or_odd(-1) returns "Odd"', {
  expect_equal(even_or_odd(-1), "Odd")
})

test_that('even_or_odd(-2) returns "Even"', {
  expect_equal(even_or_odd(-2), "Even")
})
```

---
## Code Solution

```R
even_or_odd <- function(n) {
  if (n %% 2 == 0) {
    return('Even')
  }
  else {
    return('Odd')
  }
}
```

or

```R
even_or_odd <- function(n) { 
  if (n %% 2 == 0) { return('Even') } 
  return('Odd') 
}
```

---
## Resources I used for help

https://www.geeksforgeeks.org/r-language/mathematical-computations-using-r/

https://quantifyinghealth.com/modulo-operator-in-r-examples/

https://www.geeksforgeeks.org/r-language/r-if-else-statement/

https://www.geeksforgeeks.org/r-language/functions-in-r-programming/

https://www.geeksforgeeks.org/r-language/r-boolean-logic/

---