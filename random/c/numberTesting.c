#include <stdio.h>

const char* evenOrOdd(int a) {
  if (a % 2 == 0) {
    return "Even";
  }
  else {
    return "Odd";
  }
}

const char* posOrNeg(int a) {
  if (a > 0) {
    return "Positive";
  }
  else if (a < 0) {
    return "Negative";
  }
  else {
    return "Zero";
  }
}

const char* divisibleByThree(int a) {
  int sum = 0;

  while (a > 0) {
    int digit = a % 10;
    sum += digit;
    a = a / 10;
  }

  if (sum % 3 == 0) {
    return "Divisible by Three";
  }
  else {
    return "Not Divisible by Three";
  }
}

int main() {
  int a;

  printf("Input a number: ");
  scanf("%d", &a);

  const char* evenOrOddResult = evenOrOdd(a);
  const char* posOrNegResult = posOrNeg(a);
  const char* divisibleByThreeResult = divisibleByThree(a);

  printf("The number %d is %s\n", a, evenOrOddResult);
  printf("The number %d is %s\n", a, posOrNegResult);
  printf("The number %d is %s\n", a, divisibleByThreeResult);

  return 0;
}
