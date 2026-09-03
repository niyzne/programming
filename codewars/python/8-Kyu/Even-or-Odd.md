# Even or Odd

---
## Info

Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Mathematics | Fundamentals

---
## Code

Solution

```python
def even_or_odd(number):
    pass
```

Sample Tests

```python
import codewars_test as test
from solution import even_or_odd

@test.describe("Example tests")
def example_tests():
    
    @test.it('even_or_odd(1) should return "Odd"')
    def test_positive_odd():
        test.assert_equals(even_or_odd(1), "Odd")
        
    @test.it('even_or_odd(2) should return "Even"')
    def test_positive_even():
        test.assert_equals(even_or_odd(2), "Even")

    @test.it('even_or_odd(-1) should return "Odd"')
    def test_negative_odd():
        test.assert_equals(even_or_odd(-1), "Odd")
            
    @test.it('even_or_odd(-2) should return "Even"')
    def test_negative_even():
        test.assert_equals(even_or_odd(-2), "Even")

    @test.it('even_or_odd(0) should return "Even"')
    def test_zero():
        test.assert_equals(even_or_odd(0), "Even")
```

---
## Code Solution

```python
def even_or_odd(num):
    if num % 2 == 0:
        return 'Even'
    return 'Odd'
```

---