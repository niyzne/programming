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

```go
package kata

func SeriesSum(n int) string {
  // your code here
  return ""
}
```

Sample Tests

```go
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Sample Tests", func() {
  It("should pass provided tests", func() {
     Expect(SeriesSum(1)).To(Equal("1.00"), "n = 1")
     Expect(SeriesSum(2)).To(Equal("1.25"), "n = 2")
     Expect(SeriesSum(3)).To(Equal("1.39"), "n = 3")
     Expect(SeriesSum(4)).To(Equal("1.49"), "n = 4")
  })
})
```

---
## Code Solution

```go
package kata

import "fmt"

func SeriesSum(n int) string {
  newNum := 0.0
  for i := 0; i < n; i++ {
    a := 1 / (1 + 3 * float64(i))
    newNum += a 
  }
  return fmt.Sprintf("%.2f", newNum)
}
```

---
## Resources I used for help

https://pkg.go.dev/fmt

https://programming.guide/go/round-float-2-decimal-places.html

https://golangdocs.com/for-loop-in-golang

---