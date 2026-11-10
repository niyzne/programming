#include <stdio.h>

const char* evenOrOdd(int a) {
  return a % 2 == 0 ? "Even" : "Odd";
}

const char* posOrNeg(int a) {
  return a > 0 ? "Positive" : a < 0 ? "Negative" : "Zero";
}

const char* divisibleByThree(int a) {
  return a % 3 == 0 ? "Divisible by Three" : "Not Divisible by Three";
}

const char* isPrimeNum(int a) {
  if (a == 0 || a == 1 || a < 0) {
    return "Nether a Prime nor Composite";
  }
  else {
    bool found = false;

    for (int i = 2; i < a; i++) {
      if (a % i == 0) {
        found = true;
        break;
      }
    }

    return found == true ? "Not a Prime Number" : "Prime Number";
  }
}

int main() {
  int a;

  printf("Input a number: ");
  scanf("%d", &a);

  const char* evenOrOddResult = evenOrOdd(a);
  const char* posOrNegResult = posOrNeg(a);
  const char* divisibleByThreeResult = divisibleByThree(a);
  const char* isPrimeNumResult = isPrimeNum(a);

  printf("The number %d is:\n", a);
  printf("- %s\n", evenOrOddResult);
  printf("- %s\n", posOrNegResult);
  printf("- %s\n", divisibleByThreeResult);
  printf("- %s\n", isPrimeNumResult);

  return 0;
}
