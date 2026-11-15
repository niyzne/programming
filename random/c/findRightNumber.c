#include <stdio.h>
#include <stdlib.h>

int randomNum() {
  return rand() % (20 - 1 + 1) + 1;
}

const char* numberGuess(int a) {
  int b = randomNum();
  return a > b ? "Too high!" : a < b ? "Too low!" : "Correct! You win!";
}

int main() {
  while (true) {
    int userGuess;

    printf("Guess a number in between 1 and 20: ");
    scanf("%d", &userGuess);
    if !(1 <= userGuess <= 20) {

    }

    const char* result = numberGuess(userGuess);

    printf("%s", result);
  }

  return 0;
}
