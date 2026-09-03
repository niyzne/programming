# Volume of a Cuboid

---
## Info

Bob needs a fast way to calculate the volume of a [rectangular cuboid](https://en.wikipedia.org/wiki/Rectangular_cuboid) with three values: the `length`, `width` and `height` of the cuboid.

Write a function to help Bob with this calculation.

---
Geometry | Fundamentals | Mathematics

---
## Code

Solution

```java
public class Kata {

  public static double getVolumeOfCuboid(final double length, final double width, final double height) {
    // Your code here
    return 0;
  }
  
}
```

Sample Tests

```java
import org.junit.Test;
import static org.junit.Assert.*;

public class ExampleTests {

  private static final double delta = 0.0001;
  
  @Test
  public void examples() {
      // assertEquals("expected", "actual");
      assertEquals(4, Kata.getVolumeOfCuboid(1, 2, 2), delta);
      assertEquals(63, Kata.getVolumeOfCuboid(6.3, 2, 5), delta);
  }
}
```

---
## Code Solution

```java
public class Kata {
  public static double getVolumeOfCuboid(final double l, final double w, final double h) {
    return l * w * h;
  }
}
```

---