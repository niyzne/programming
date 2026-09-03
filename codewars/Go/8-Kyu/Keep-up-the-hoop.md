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

```go
package kata

func HoopCount(n int) string {
  // your code goes here
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

var _ = Describe("Example tests", func() {
	It("Three hoops is not enough", func() {
		Expect(HoopCount(3)).To(Equal("Keep at it until you get it"))
	})
  
	It("Twelve hoops is good", func() {
		Expect(HoopCount(12)).To(Equal("Great, now move on to tricks"))
	})  
})
```

---
## Code Solution

```go
package kata

func HoopCount(n int) string {
  if n >= 10 { return "Great, now move on to tricks" }
  return "Keep at it until you get it"
}
```

---