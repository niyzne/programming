# Grasshopper - Messi goals function

---
## Info

# Messi goals function

[Messi](https://en.wikipedia.org/wiki/Lionel_Messi) is a soccer player with goals in three leagues:

- LaLiga
- Copa del Rey
- Champions

Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

```
5, 10, 2  -->  17
```

---
Fundamentals

---
## Code

Solution

```python
def goals(laLiga, copaDelRey, championsLeague):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import goals

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(goals(0, 0, 0), 0)
        test.assert_equals(goals(5, 10, 2), 17)
```

---
## Code Solution

```python
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
```

---