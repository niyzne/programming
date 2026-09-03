# Keep up the hoop

---
## Info

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (`n`) how many times the hoop goes round and it will return him an encouraging message:

- If Alex gets 10 or more hoops, return the string `"Great, now move on to tricks"`.
- If he doesn't get 10 hoops, return the string `"Keep at it until you get it"`.

---
Fundamentals

---
## Code

Solution

```R
hoop_count <- function(n){
 
}
```

Sample Tests

```R
test_that('Basic tests', {
  expect_equal(hoop_count(6),"Keep at it until you get it" ) 
  expect_equal(hoop_count(10),"Great, now move on to tricks" ) 
  expect_equal(hoop_count(22), "Great, now move on to tricks")
})
```

---
## Code Solution

```R
hoop_count <- function(n){
  if (n >= 10) { return('Great, now move on to tricks') }
  return('Keep at it until you get it')
}
```

---
## Resources I used for help

https://www.geeksforgeeks.org/r-language/r-if-else-statement/

---