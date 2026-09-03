# L1 - Set Alarm

---
## Info

Write a function named `setAlarm`/`set_alarm`/`set-alarm`/`setalarm` (depending on language) which receives two parameters. The first parameter, `employed`, is true whenever you are employed and the second parameter, `vacation` is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

```
employed | vacation 
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false
```

---
Fundamentals | Logic

---
## Code

Solution

```python
def set_alarm(employed, vacation):
    # Your code here
```

Sample Tests

```python
import codewars_test as test
from solution import set_alarm

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(set_alarm(True, True), False, "Fails when input is True, True")
        test.assert_equals(set_alarm(False, True), False, "Fails when input is False, True")
        test.assert_equals(set_alarm(False, False), False, "Fails when input is False, False")
        test.assert_equals(set_alarm(True, False), True, "Fails when input is True, False")
```

---
## Code Solution

```python
def set_alarm(employed, vacation):
    if employed and vacation:
        return False
    elif employed and not vacation:
        return True
    elif not employed and vacation:
        return False
    else:
        return False
```

realized i can do:

```python
def set_alarm(employed, vacation):
	return employed and not vacation
```

---
