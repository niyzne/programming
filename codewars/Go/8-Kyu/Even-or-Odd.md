# Even or Odd

---
## Info

Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Fundamentals | Mathematics

---
## Code

Solution

```go
package kata

func EvenOrOdd(number int) string {
  return "TODO" // your code here
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
var _ = Describe("Test Example", func() {
  
  It("should return \"Odd\" for odd positive numbers", func() {
    Expect(EvenOrOdd(1)).To(Equal("Odd"))
  })
  
  It("should return \"Even\" for even positive numbers", func() {
    Expect(EvenOrOdd(2)).To(Equal("Even"))
  })
  
  It("should return \"Odd\" for odd negative numbers", func() {
    Expect(EvenOrOdd(-1)).To(Equal("Odd"))
  })
  
  It("should return \"Even\" for even negative numbers", func() {
    Expect(EvenOrOdd(-2)).To(Equal("Even"))
  })
  
  It("should return \"Even\" for zero", func() {
    Expect(EvenOrOdd(0)).To(Equal("Even"))
  })
})
```

---
## Code Solution

```go
package kata

func EvenOrOdd(num int) string {
  if num % 2 == 0 { return "Even" } 
  return "Odd"
}
```

---