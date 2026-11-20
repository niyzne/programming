import java.util.Scanner;

public class numberTesting {
  static int multByTwo(int a) {
    return a * 2;
  }

  static int divideByThree(int a) {
    return a / 3;
  }

  public static void main(String[] args) {
    Scanner number = new Scanner(System.in);
    System.out.print("Enter a number: ");

    String num = number.nextLine();
    int intNumber = Integer.parseInt(num);

    System.out.println(multByTwo(intNumber));
    System.out.println(divideByThree(intNumber));
  }
}
