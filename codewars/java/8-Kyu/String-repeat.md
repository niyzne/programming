# String repeat

---
## Info

Write a function that accepts a non-negative integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.

### Examples (input -> output)

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

---
Fundamentals | Strings

---
## Code

Solution

```java
public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        return "";
    }
}
```

Sample Tests

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test public void test4a() {
        assertEquals("aaaa", Solution.repeatStr(4, "a"));
    }
    @Test public void test3Hello() {
        assertEquals("HelloHelloHello", Solution.repeatStr(3, "Hello"));
    }
    @Test public void test5empty() {
        assertEquals("", Solution.repeatStr(5, ""));
    }
    @Test public void test0kata() {
        assertEquals("", Solution.repeatStr(0, "kata"));
    }
    @Test public void test0empty() {
        assertEquals("", Solution.repeatStr(0, ""));
    }
    @Test public void test6I() {
        assertEquals("IIIIII", Solution.repeatStr(6, "I"));
    }
    @Test public void test5Hello() {
        assertEquals("HelloHelloHelloHelloHello", Solution.repeatStr(5, "Hello"));
    }
}
```

---
## Code Solution

```java
public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        if (repeat <= 0 || string == null) {
            return "";
        }
        return string.repeat(repeat);
    }
}
```

---