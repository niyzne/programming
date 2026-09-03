# Keep up the hoop

---
## Info

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (`n`) how many times the hoop goes round and it will return him an encouraging message:

- If Alex gets 10 or more hoops, return the string `"Great, now move on to tricks"`.
- If he doesn't get 10 hoops, return the string `"Keep at it until you get it"`.

---
Fundamentals

---
## Code

Solution

```java
public class HelpAlex{
  public static String hoopCount(int n){
   return null;
  }
}
```

Sample Tests

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class HoopCountTest {
    @Test
    public void testHoopCount(){
        assertEquals("Great, now move on to tricks", HelpAlex.hoopCount(11));
        assertEquals("Keep at it until you get it", HelpAlex.hoopCount(7));
    }
}
```

---
## Code Solution

```java
public class HelpAlex{
  public static String hoopCount(int n){
   if (n >= 10) { return "Great, now move on to tricks"; }
    return "Keep at it until you get it"; }
}
```

---
## Resources I used for help

https://www.w3schools.com/java/java_conditions.asp

https://stackoverflow.com/questions/36393448/java-return-statement-after-if-else-if-else-loop

---