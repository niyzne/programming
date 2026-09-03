# Invert values

---
## Info

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
```

---
Lists | Fundamentals | Arrays

---
## Code

Solution

```R
invert <- function(vec){
 
}
```

Sample Tests

```R
test_that('Basic tests', {
  expect_equal(invert(c(1,2,3,4,5)),c(-1,-2,-3,-4,-5))
  expect_equal(invert(c(1,-2,3,-4,5)), c(-1,2,-3,4,-5))
  expect_equal(invert(numeric()), numeric())
  expect_equal(invert(c(0)), c(0))
})
```

---
## Code Solution

```R
invert <- function(vec){
  -vec
}
```

---
## Resources I used for help

https://www.dataquest.io/blog/for-loop-in-r/

https://www.geeksforgeeks.org/r-language/looping-through-a-list-in-r/

https://www.geeksforgeeks.org/r-language/finding-inverse-of-a-matrix-in-r-programming-inv-function/

---