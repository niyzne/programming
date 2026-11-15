#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// const char* numberGuess(int guess, int randomNumber) {
void numberGuess(int randomNumber) {
  int numberofguess = 0;

  int guess = checkNumber();

  while (guess != randomNumber) {
    if (numberofguess > 5) {
        printf("You Loose!");
        break;
    }

    if (guess > randomNumber) {
      printf("Too high!\n");
      numberofguess++;
    }
    else if (guess < randomNumber) {
      printf("Higher number please!\n");
      numberofguess++;
    }
    else {
      printf("You guessed the number %d in %d attempts!\n", randomNumber, numberofguess);
    }
    int guess = checkNumber();
  }
}

int checkNumber() {
  while (true) {
    int userGuess;

    printf("Guess a number in between 1 and 20: ");
    int input = scanf("%d", &userGuess);
    while ((input != 1) || (userGuess < 1 || userGuess > 20)) {
      printf("Wrong input, try again: ");
      input = scanf("%d", &userGuess);
      break;
    }
    break;
  }
  return userGuess;
}

int main() {
  srand(time(NULL));
  int randomNumber = rand() % 20 + 1;

  // int userGuess = checkNumber();

  // const char* result = numberGuess(userGuess, randomNumber);

  // const char* result = numberGuess(randomNumber);
  numberGuess(randomNumber);

  printf("%s\n", result);
  }

  return 0;
}

// a bit broken but will come back to it later
