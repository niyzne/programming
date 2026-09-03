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

```cpp
#include <string>

std::string hoop_count(unsigned n) {
   return ""; // Your code here
}
```

Sample Tests

```cpp
// TODO: Replace examples and use TDD by writing your own tests

std::string hoop_count(unsigned n);

Describe(Sample_Tests) 
{  
	It(Ten_hoops) 
  {
		Assert::That( hoop_count( 10 ), Equals( "Great, now move on to tricks" ));
	}
  
  It(Nine_hoops) 
  {
		Assert::That( hoop_count( 9 ), Equals( "Keep at it until you get it" ));
	}
};
```

---
## Code Solution

```cpp
#include <string>

std::string hoop_count(unsigned n) {
  if (n >= 10) { return "Great, now move on to tricks"; }
  return "Keep at it until you get it";
}
```

---