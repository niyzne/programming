# Keep Hydrated!

---
## Info

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded _down_.

For example:

```
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
```

---
Algorithms | Mathematics | Fundamentals

---
## Code

Solution

```R
litres <- function(time) {}
```

Sample Tests

```R
expect_equal(litres(2), 1)
expect_equal(litres(1.4), 0)
expect_equal(litres(12.3), 6)
expect_equal(litres(0.82), 0)
expect_equal(litres(11.8), 5)
expect_equal(litres(1787), 893)
expect_equal(litres(0), 0)
```

---
## Code Solution

```R
litres <- function(time) {
  floor(time * 0.5)
}
```

---