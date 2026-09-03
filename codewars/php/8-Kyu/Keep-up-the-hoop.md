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

```php
function hoopCount ($n)
{
    # your code here
}
```

Sample Tests

```php
<?php use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    public function test_9_hoops() {
      $this->assertEquals("Keep at it until you get it", hoopCount(9));
    }
    public function test_10_hoops() {
      $this->assertEquals("Great, now move on to tricks", hoopCount(10));
    }
}
```

---
## Code Solution

```php
function hoopCount ($n) {
  if ($n >= 10) { return 'Great, now move on to tricks'; } 
  return 'Keep at it until you get it';
}
```

---
## Resources I used for help

https://www.w3schools.com/php/php_if_else.asp

https://www.php.net/manual/en/control-structures.else.php

---