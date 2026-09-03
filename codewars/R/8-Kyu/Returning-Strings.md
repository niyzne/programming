# Returning Strings

---
## Info

Create a function that accepts a parameter representing a `name` and returns the message: `"Hello, <name> how are you doing today?"`.

_[Make sure you type the exact thing I wrote or the program may not execute properly]_

---
Strings | Fundamentals

---
## Code

Solution

```R
greet <- function(name) {
    # TODO: 
}
```

Sample Tests

```R
test_that("example test cases", {
    expect_equal(greet('Ryan'), 'Hello, Ryan how are you doing today?')
})
```

---
## Code Solution

```R
library(glue)

greet <- function(name) {
  sprintf("Hello, %s how are you doing today?", name)
}
```

---