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

int main() {
  int a;

  printf("Input a number: ");
  scanf("%d", &a);

  const char* evenOrOddResult = evenOrOdd(a);
  const char* posOrNegResult = posOrNeg(a);

  printf("The number %d is %s\n", a, evenOrOddResult);
  printf("The number %d is %s\n", a, posOrNegResult);

  return 0;
}
