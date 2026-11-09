#include <stdio.h>
#include <string.h>

int intToBin(int a) {
  char newNum[100] = "";

  while (a > 0) {
    int num = a % 2;
    strcat(newNum, num);
  }

  return newNum;
}

int main() {
  int a;

  printf("Input a number: ");
  scanf("%d", &a);

  int intToBinResult = intToBin(a);

  printf("The number %d is %d in binary", a, intToBinResult);

  return 0;
}

// this project put on hold
