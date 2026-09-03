# Even or Odd

---
## Info

Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Fundamentals | Mathematics

---
## Code

Solution

```cpp
#include <string>

std::string even_or_odd(int number) 
{
  return "";
}
```

Sample Tests

```cpp
#include <string>

std::string even_or_odd(int number);

Describe(example_tests)
{
    It(zero)
    {
        Assert::That(even_or_odd(0), Equals("Even"), ExtraMessage("Incorrect answer for number=0"));
    }
  
    It(positive_odd_numbers)
    {
        Assert::That(even_or_odd( 1), Equals("Odd"), ExtraMessage("Incorrect answer for number=1"));
        Assert::That(even_or_odd(21), Equals("Odd"), ExtraMessage("Incorrect answer for number=21"));
    }  
  
    It(positive_even_numbers)
    {
        Assert::That(even_or_odd(  2), Equals("Even"), ExtraMessage("Incorrect answer for number=2"));
        Assert::That(even_or_odd(100), Equals("Even"), ExtraMessage("Incorrect answer for number=100"));
    }
  
    It(negative_odd_numbers)
    {
        Assert::That(even_or_odd( -1), Equals("Odd"), ExtraMessage("Incorrect answer for number=-1"));
        Assert::That(even_or_odd(-21), Equals("Odd"), ExtraMessage("Incorrect answer for number=-21"));
    }  
  
    It(negative_even_numbers)
    {
        Assert::That(even_or_odd(  -2), Equals("Even"), ExtraMessage("Incorrect answer for number=-2"));
        Assert::That(even_or_odd(-100), Equals("Even"), ExtraMessage("Incorrect answer for number=-100"));
    }  
};
```

---
## Code Solution

```cpp
#include <string>

std::string even_or_odd(int num) 
{
  if (num % 2 == 0) {
    return "Even";
  }
  return "Odd";
}
```

---