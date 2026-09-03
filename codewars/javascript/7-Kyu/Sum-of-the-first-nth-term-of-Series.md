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

```js
function SeriesSum(n) {
  // Happy Coding ^_^
}
```

Sample Tests

```js
const { assert } = require('chai');

describe("Sample tests", () => {
  it("n = 1", () => {
    let actual = SeriesSum(1);
    checkReturnValue(actual);
    assert.strictEqual(actual,  "1.00", "n = 1")
  });
  it("n = 2", () => assert.strictEqual(SeriesSum(2),  "1.25", "n = 2"));
  it("n = 3", () => assert.strictEqual(SeriesSum(3),  "1.39", "n = 3"));
  it("n = 4", () => assert.strictEqual(SeriesSum(4),  "1.49", "n = 4"));
});

function checkReturnValue(actual) {
  assert.isDefined(actual, "Your function did not return a value. Did you log it to console instead?");
}
```

---
## Code Solution

```js
function SeriesSum(n) {
  newNum = 0
  
  for (i = 0; i < n; i++) {
    a = 1 / (1 + 3 * i);
    newNum += a
  }
  
  return newNum.toFixed(2);
}
```

---
## Resources I used for help

https://www.w3schools.com/js/js_type_conversion.asp

https://www.geeksforgeeks.org/javascript/javascript-program-for-sum-of-n-terms-of-arithmetic-progression/

https://stackoverflow.com/questions/11686724/adding-numbers-in-for-loop-javascript

---