# Sum of the first nth term of Series

---
## Task

Your task is to write a function which returns the `n`-th term of the following series, which is the sum of the first `n` terms of the sequence (`n` is the input parameter).

Series:1+14+17+110+113+116+…\mathrm{Series:}\quad 1 + \frac14 + \frac17 + \frac1{10} + \frac1{13} + \frac1{16} + \dotsSeries:1+41​+71​+101​+131​+161​+…

You will need to figure out the rule of the series to complete this.
## Rules

- You need to round the answer to 2 decimal places and return it as String.
- If the given value is `0` then it should return `"0.00"`.
- You will only be given Natural Numbers as arguments.
## Examples (Input --> Output)

```
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
```

---
Fundamentals

---
## Code

Solution

```java
public class NthSeries {
	public static String seriesSum(int n) {
		// Happy Coding ^_^
        return "";
	}
}
```

Sample Tests

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class NthSeriesTest {
	@Test
	public void sampleTests() {
		doTest( 0, "0.00");
		doTest( 5, "1.57");
		doTest( 9, "1.77");
		doTest(15, "1.94");
		doTest(39, "2.26");
		doTest(58, "2.40");
	}
    private static void doTest(int n, String expected) {
        String message = "n = " + n + "\n";
        String actual = NthSeries.seriesSum(n);
        assertEquals(expected, actual, message);
    }
}
```

---
## Code Solution

```java
public class NthSeries {
	public static String seriesSum(int n) {
    double newNum = 0.0;
    for (int i = 0; i < n; i++) {
      double a = 1 / (1 + 3 * (double)(i));
      newNum += a;
    }
    return String.format("%.2f", newNum);
  }
}
```

---
## Resources I used for help

https://www.geeksforgeeks.org/java/java-program-to-convert-double-to-string/

https://codegym.cc/groups/posts/how-to-convert-int-to-double-in-java

https://beginnersbook.com/2018/09/java-convert-int-to-double/

https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Java-double-precision-2-decimal-places-example-float-range-math-jvm

---