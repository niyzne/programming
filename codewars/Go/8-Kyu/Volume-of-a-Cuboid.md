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

```go
package kata


func GetVolumeOfCuboid(length, width, height float64) float64 {
  return 0.0
}
```

Sample Tests

```go
// TODO: replace with your own tests (TDD). An example to get you started is included below.
// Ginkgo BDD Testing Framework <http://onsi.github.io/ginkgo/>
// Gomega Matcher Library <http://onsi.github.io/gomega/>

package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
  "math"
  "fmt"
)

func assertApproxEquals(actual, expected float64) (passed bool) {
  if expected == 0 {
    passed = math.Abs(actual) <= 1e-10
  } else {
    passed = math.Abs((actual - expected) / expected) <= 1e-10
  }
  if ! passed {
    fmt.Printf("Expected value close to %f, but got %f", expected, actual)
  }
  return
}

func dotest(a, b, c, d float64) {
  Expect(assertApproxEquals(GetVolumeOfCuboid(a,b,c), d)).To(BeTrue(), "With length = %f, width = %f, height = %f", a, b, c)
}

var _ = Describe("Tests", func() {
     It("Sample tests", func() {
       dotest(1.0,2.0,2.0,4.0)
       dotest(6.3,2.0,5.0,63.0)
     })
})
```

---
## Code Solution

```go
package kata

func GetVolumeOfCuboid(l, w, h float64) float64 {
  return l * w * h
}
```

---