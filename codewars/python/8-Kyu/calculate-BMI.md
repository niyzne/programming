# Calculate BMI

---
## Info

Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

---
Fundamentals

---
## Code

Solution

```python
def bmi(weight, height):
    #your code here
```

Sample Tests

```python
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bmi(50, 1.80), "Underweight", "For weight = 50 and height = 1.80")
        test.assert_equals(bmi(80, 1.80), "Normal", "For weight = 80 and height = 1.80")
        test.assert_equals(bmi(90, 1.80), "Overweight", "For weight = 90 and height = 1.80")
        test.assert_equals(bmi(100, 1.80), "Obese", "For weight = 100 and height = 1.80")
```

---
## Code Solution

```python
def bmi(weight, height):
    bmi = (weight / (height ** 2))
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
```

---