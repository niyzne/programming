import java.util.Scanner;

public class numberTesting {

  static int multByTwo(int a) {
    return a * 2;
  }

  static int divideByThree(int a) {
    return a / 3;
  }

  public static String evenOrOdd(int a) {
    return (a % 2 == 0) ? "Even" : "Odd";
  }

  public static String posOrNeg(int a) {
    return (a > 0) ? "Positive" : (a < 0) ? "Negative" : "Zero";
  }

  public static String divisibleByThree(int a) {
    return (a % 3 == 0) ? "Divisible by Three" : "Not Divisible by Three";
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

      return (found == true) ? "Not a Prime Number" : "Prime Number";
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
