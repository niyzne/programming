# Sum The Strings

---
## Info

Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (**Input1, Input2 -->Output**)

```
"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
```

Notes:

- If either input is an empty string, consider it as zero.
- Inputs and the expected output will never exceed the signed 32-bit integer limit (`2^31 - 1`)

---
Fundamentals

---
## Code

Solution

```js
function sumStr(a,b) {
  
}
```

Sample Tests

```js
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests", () => {
  it("Tests example test cases", () => {
    assert.strictEqual(sumStr("4","5"), "9");
    assert.strictEqual(sumStr("34","5"), "39");
  });
});
```

---
## Code Solution

```js
function sumStr(a,b) {
  return String(parseInt(a || '0') + parseInt(b || '0'))
}
```

---
## Resources I used for help

https://bobbyhadz.com/blog/javascript-add-strings-as-numbers

https://blog.finxter.com/5-best-ways-to-add-two-numbers-represented-as-strings-in-python/

---