# Function 1 - hello world

---
## Info

Make a simple function called `greet` that returns the most-famous "hello world!".

### Style Points

Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" you can think of? What is a "hello world" solution you would want to show your friends?

---
Fundamentals

---
## Code

Solution

```python
# Write a function `greet` that returns "hello world!"

```

Sample Tests

```python
import codewars_test as test
from solution import greet

@test.describe("Greet function")
def _():
    @test.it("Making sure greet exists")
    def _():
        try:
            test.expect(greet)
        except NameError:
            test.fail("Greet doesn't exist")
    @test.it("Testing that it returns hello world!")
    def _():
        test.assert_equals(greet(), "hello world!", "Greet doesn't return hello world!")
```

---
## Code Solution

```python
def greet():
    greeting = 'hello world!'
    
    rev_greeting = greeting[::-1]
    
    parts = []

    for character in rev_greeting:
        parts.insert(0, character)
    result = "".join(parts)

    return result
```

or

```python
def greet():
    greeting = 'hello world!'
    return greeting[::-1][::-1]
```

or even more purposely over complicated

```python
def greet():
    greeting = 'hello world!'
    
    rev_greeting = greeting[::-1]
    
    parts = []

    for character in rev_greeting:
        parts.insert(0, character)
    result = "".join(parts)

    return result[::-1][::-1]
```

---