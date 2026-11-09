#include <stdio.h>

const char* evenOrOdd(int a) {
  if (a % 2 == 0) {
    return "Even";
  }
  else {
    return "Odd";
  }
}

int main() {
  int a;

  printf("Input a number: ");
  scanf("%d", &a);

  const char* result = evenOrOdd(a);

  printf("The number %d is %s\n", a, result);

  return 0;
}
