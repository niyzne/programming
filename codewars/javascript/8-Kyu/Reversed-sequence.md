# Reversed sequence

---
## Info

Build a function that returns an array of integers from n to 1 where `n>0`.

Example : `n=5` --> `[5,4,3,2,1]`

---
Fundamentals

---
## Code

Solution

```js
const reverseSeq = n => {
  return [];
};
```

Sample Tests

```js
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("reverseSeq", function() {
  it("Sample Test", function() {
    assert.deepEqual(reverseSeq(5), [5, 4, 3, 2, 1]);
  });
});
```

---
## Code Solution

```js
const reverseSeq = n => {
    let arrayList = [];
    for (let i = 1; i <= n; i++) {
        arrayList.push(i);
    }
    return arrayList.reverse();
};
```

---
## Resources I used for help

https://www.xjavascript.com/blog/how-to-print-elements-from-an-array-with-javascript/

https://www.w3schools.com/js/js_loop_for.asp

https://stackoverflow.com/questions/3010840/how-to-loop-through-the-items-of-an-array-in-javascript

https://itsourcecode.com/javascript-tutorial/how-to-return-an-array-in-javascript/

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse

---