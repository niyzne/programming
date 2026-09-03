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

```cpp
double getVolumeOfCuboid(double length, double width, double height) {
  // Your code here...
    return 0.0;
}
```

Sample Tests

```cpp
#include <fmt/core.h>
#include <string>

Describe(GetVolume)
{
public:
    It(SampleTests)
    {
        doTest(1, 2, 2,4);
        doTest(6.3, 2, 5,63);
        doTest(2, 5, 6,60);
        doTest(6.3, 3, 5,94.5);
    }

private:
    void doTest(double length, double width, double height, double expected)
    {
        double actual = getVolumeOfCuboid(length, width, height);
        std::string message = fmt::format(
            "Length: {:.17g}, Width: {:.17g}, Height: {:.17g}\n",
            length, width, height);
        Assert::That(actual, EqualsWithDelta(expected, 1e-3), ExtraMessage(message));
    }
};
```

---
## Code Solution

```cpp
double getVolumeOfCuboid(double l, double w, double h) {
  return l * w * h;
}
```

---