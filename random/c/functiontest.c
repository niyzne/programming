#include <stdio.h>

int add(int a, int b) {
  return a + b;
}

int main() {
  int a;
  int b;

  printf("Input number a: ");
  scanf("%d", &a);

  printf("Input number b: ");
  scanf("%d", &b);

  int result = add(a, b);
  printf("The sum of %d and %d is %d\n", a, b, result);

  return 0;
}
