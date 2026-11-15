import java.util.Scanner;

public class main {
  public static void helloWorld() {
    System.out.println("Hello World");
  }

  public static void multByTwo(int a) {
    System.out.println(a * 2);
  }

  public static String printMsg(String name) {
    String myStr = "Hello %s.";
    String result = String.format(myStr, name);
    return result;
  }

  public static void main(String[] args) {
    helloWorld();
    int num = 15;
    multByTwo(num);

    Scanner username = new Scanner(System.in);
    System.out.println("Enter Name: ");

    String name = username.nextLine();
    System.out.println(printMsg(name));
  }
}
