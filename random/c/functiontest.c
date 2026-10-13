#include <stdio.h>

int add(int a, int b) {
  return a + b;
}

int main() {
  int a;
  int b;

  printf("Input number a: \n");
  scanf("%d", &a);

  printf("Input number b: \n");
  scanf("%d", &b);

  int result = add(a, b);
  printf("%d\n", result);

  return 0;
}
