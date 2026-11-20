import java.util.Scanner;

public class numberTesting {

  static int multByTwo(int a) {
    return a * 2;
  }

  static int divideByThree(int a) {
    return a / 3;
  }

  public static String evenOrOdd(int a) {
    if (a % 2 == 0) {
      return "Even";
    }
    else {
      return "Odd";
    }
  }

  public static String posOrNeg(int a) {
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

  public static String divisibleByThree(int a) {
    if (a % 3 == 0) {
      return "Divisible by Three";
    }
    else {
      return "Not Divisible by Three";
    }
  }

  public static String isPrimeNum(int a) {
    if (a == 0 || a == 1 || a < 0) {
      return "Nether a Prime nor Composite";
    }
    else {
      boolean found = false;

      for (int i = 2; i < a; i++) {
        if (a % i == 0) {
          found = true;
          break;
        }
      }

      if (found == true) {
        return "Not a Prime Number";
      }
      else {
        return "Prime Number";
      }
    }
  }

  public static void main(String[] args) {
    Scanner number = new Scanner(System.in);
    System.out.print("Enter a number: ");

    String num = number.nextLine();
    int intNumber = Integer.parseInt(num);

    System.out.println(multByTwo(intNumber));
    System.out.println(divideByThree(intNumber));
    System.out.println(evenOrOdd(intNumber));
    System.out.println(posOrNeg(intNumber));
    System.out.println(divisibleByThree(intNumber));
    System.out.print(isPrimeNum(intNumber));
  }
}
