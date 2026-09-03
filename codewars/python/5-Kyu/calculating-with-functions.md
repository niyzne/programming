# Calculating with Functions

---
## Info

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```python
seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3
```

Requirements:

- There must be a function for each number from 0 ("zero") to 9 ("nine")
- There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Division should be **integer division**. For example, this should return `2`, not `2.666666...`:

```python
eight(divided_by(three()))
```

---
Functional Programming

---
## Code

Solution

```python
def zero(): pass #your code here
def one(): pass #your code here
def two(): pass #your code here
def three(): pass #your code here
def four(): pass #your code here
def five(): pass #your code here
def six(): pass #your code here
def seven(): pass #your code here
def eight(): pass #your code here
def nine(): pass #your code here

def plus(): pass #your code here
def minus(): pass #your code here
def times(): pass #your code here
def divided_by(): pass #your code here
```

Sample Tests

```python
import codewars_test as test
from solution import *

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(seven(times(five())), 35)
        test.assert_equals(four(plus(nine())), 13)
        test.assert_equals(eight(minus(three())), 5)
        test.assert_equals(six(divided_by(two())), 3)
```

---
## Code Solution

```python
def zero(op=None):
    if op is None:
        return 0
    return op(0)

def one(op=None):
    if op is None:
        return 1
    return op(1)
    
def two(op=None):
    if op is None:
        return 2
    return op(2)

def three(op=None):
    if op is None:
        return 3
    return op(3)
    
def four(op=None):
    if op is None:
        return 4
    return op(4)

def five(op=None):
    if op is None:
        return 5
    return op(5)

def six(op=None):
    if op is None:
        return 6
    return op(6)

def seven(op=None):
    if op is None:
        return 7
    return op(7)

def eight(op=None):
    if op is None:
        return 8
    return op(8)

def nine(op=None):
    if op is None:
        return 9
    return op(9)

def plus(rnum):
    return lambda lnum: lnum + rnum

def minus(rnum):
    return lambda lnum: lnum - rnum

def times(rnum):
    return lambda lnum: lnum * rnum

def divided_by(rnum):
    return lambda lnum: lnum // rnum
```

---
## Resources I used for help

https://www.programiz.com/python-programming/examples/calculator

https://www.geeksforgeeks.org/python/make-simple-calculator-using-python/

---