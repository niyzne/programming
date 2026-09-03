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

```ts
export function SeriesSum(n:number):string
{
  // Happy Coding ^_^
}
```

Sample Tests

```ts
import solution = require('./solution');
import {assert} from "chai";

describe("solution", function(){
  it("Basic Tests", function() {
    assert.equal(solution.SeriesSum(1), "1.00");
    assert.equal(solution.SeriesSum(2), "1.25");
    assert.equal(solution.SeriesSum(3), "1.39");
    assert.equal(solution.SeriesSum(4), "1.49");
  });
});
```

---
## Code Solution

```ts
export function SeriesSum(n:number):string
{
  let newNum = 0
  for (let i = 0; i < n; i++) {
    let a = 1 / (1 + 3 * i)
    newNum += a
  }  
  return newNum.toFixed(2)
}
```

---