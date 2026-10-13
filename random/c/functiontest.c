#include <stdio.h>

int add(int a, int b) {
  return a + b;
}

int sub(int a, int b) {
  return a - b;
}

int mult(int a, int b) {
  return a * b;
}

int div(int a, int b) {
  return a / b;
}

int main() {
  int a;
  int b;

  printf("Input number a: ");
  scanf("%d", &a);

  printf("Input number b: ");
  scanf("%d", &b);

  int addResult = add(a, b);
  int subResult = sub(a, b);
  int multResult = mult(a, b);
  int divResult = div(a, b);

  printf("Adding %d and %d is %d\n", a, b, addResult);
  printf("Subtracting %d from %d is %d\n", b, a, subResult);
  printf("Multiplying %d and %d is %d\n", a, b, multResult);
  printf("Diving %d by %d is %d\n", a, b, divResult);

  return 0;
}
