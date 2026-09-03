# Transportation on vacation

---
## Info

After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).

---
Fundamentals

---
## Code

Solution

```python
def rental_car_cost(d):
    # your code
```

Sample Tests

```python
import codewars_test as test
from solution import rental_car_cost

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(rental_car_cost(1),40)
        test.assert_equals(rental_car_cost(4),140)
        test.assert_equals(rental_car_cost(7),230)
        test.assert_equals(rental_car_cost(8),270)
```

---
## Code Solution

```python
def rental_car_cost(days):
    day = 0
    for day in range(days):
        day += 1
    
    total = day * 40
    
    if day >= 7:
        total -= 50
    elif day >= 3:
        total -= 20
    
    return total
```

---