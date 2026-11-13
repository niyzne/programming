#include <stdio.h>

const char* numberGuess(int a) {
  int b = 5;
  return a > b ? "Too high!" : a < b ? "Too low!" : "Correct! You win!";
}

int main() {
  int a;

  printf("Guess number: ");
  scanf("%d", &a);

  const char* result = numberGuess(a);

  printf("%s", result);

  return 0;
}
