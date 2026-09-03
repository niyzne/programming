# Even or Odd

---
## Info

Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Fundamentals | Mathematics

---
## Code

Solution

```c
const char* even_or_odd(int number)
{
  // return a statically allocated string,
  // for example a string literal
  return "";
}
```

Sample Tests

```c
#include <criterion/criterion.h>

static void do_test (int number, const char *expected);

Test(SampleTests, Zero, .description = "Test zero")
{
  do_test(0, "Even");
}

Test(SampleTests, PositiveOdd, .description = "Test positive odd numbers")
{
  do_test( 1, "Odd");
  do_test(21, "Odd");
}

Test(SampleTests, PositiveEven, .description = "Test positive even numbers")
{
  do_test(  2, "Even");
  do_test(100, "Even");
}

Test(SampleTests, NegativeOdd, .description = "Test negative odd numbers")
{
  do_test( -1, "Odd");
  do_test(-21, "Odd");
}

Test(SampleTests, NegativeEven, .description = "Test negative even numbers")
{
  do_test(  -2, "Even");
  do_test(-100, "Even");
}

extern const char* even_or_odd(int number);

static void do_test (int number, const char *expected)
{
  const char *actual = even_or_odd(number);
  cr_assert_str_eq(actual, expected,
    "Incorrect answer for number=%d, expected \"%s\", but got \"%s\"",
    number, expected, actual
  );
}
```

---
## Code Solution

```c
const char* even_or_odd(int n) {
  if (n % 2 == 0) { return "Even"; }
  return "Odd";
}
```

---