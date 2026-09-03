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

```c
double getVolumeOfCuboid(double length, double width, double height) {
  // Your code here...
    return 0.0;
}
```

Sample Tests

```c
#include <criterion/criterion.h>

double getVolumeOfCuboid(double length, double width, double height);
static void doTest(double length, double width, double height, double expected);

Test(testSuite, sampleTests) {
    doTest(1, 2, 2, 4);
    doTest(6.3, 2, 5, 63);
    doTest(2, 5, 6, 60);
    doTest(6.3, 3, 5, 94.5);
}

static void doTest(double length, double width, double height, double expected) {
    double actual = getVolumeOfCuboid(length, width, height);
    cr_assert_float_eq(actual, expected, 1e-3,
        "length = %.17g; width = %.17g; height = %.17g\n"
        "expected = %.17g\nactual = %.17g",
        length, width, height, expected, actual
    );
}
```

---
## Code Solution

```c
double getVolumeOfCuboid(double l, double w, double h) {
  return l * w * h;
}
```

---