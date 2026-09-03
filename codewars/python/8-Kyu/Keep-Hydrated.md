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

```python
def litres(time):
    return 0
```

Sample Tests

```python
import codewars_test as test
from solution import litres

@test.describe('Fixed tests')
def basic_tests():
    
    @test.it('Basic Test Cases')
    def basic_tests():
        test.assert_equals(litres(0), 0, 'litres(0) should return 0')
        test.assert_equals(litres(1), 0, 'litres(1) should return 0')
        test.assert_equals(litres(2), 1, 'litres(2) should return 1')
        test.assert_equals(litres(3), 1, 'litres(3) should return 1')
        test.assert_equals(litres(4), 2, 'litres(4) should return 2')

    @test.it('Fixed Test Cases')
    def fixed_tests():
        test.assert_equals(litres(1.4), 0, 'litres(1.4) should return 0')
        test.assert_equals(litres(12.3), 6, 'litres(12.3) should return 6')
        test.assert_equals(litres(0.82), 0, 'litres(0.82) should return 0')
        test.assert_equals(litres(11.8), 5, 'litres(11.8) should return 5')
        test.assert_equals(litres(1787), 893, 'litres(1787) should return 893')
```

---
## Code Solution

```python
def litres(time):
    return int(time * 0.5)
```

---