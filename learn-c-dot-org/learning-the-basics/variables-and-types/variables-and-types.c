#include <stdio.h>

/*
Integers:
- whole positive/negative nums
- defined using: char, int, short, long, or long long

Unsigned integers:
- whole nums which can be only positive
- defined using: unsigned char, unsigned int, unsigned short, unsigned long, unsighned long long

Floating point numbers
- real numbers (numbers with fractions).
- Defined using: float and double.

Booleans
- true or false. 
- Defined using bool. 
- In older versions of C, the char type was used to represent booleans.
*/

int main() {
  int a = 10, b = 5, c = 7;
  int d = a + b * c;
  printf("%d\n", d); // "%d" is a format specifier, in this case, int

  float e = 10.3, f = 11.3, g = 11.42;
  float h = e + f / g;
  printf("%f\n", h); // "%f" is a format specifier, in this case, float


  double i = 10.3, j = 11.3, k = 11.42;
  double l = i * j / k;
  printf("%f\n", l); // "%f" is a format specifier, in this case, double

  return 0; // means program has finished successfully
}
