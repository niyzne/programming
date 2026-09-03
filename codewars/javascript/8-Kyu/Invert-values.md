# Invert values

---
## Info

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
```

---
Lists | Fundamentals | Arrays

---
## Code

Solution

```js
function invert(array) {
   return ;
}
```

Sample Tests

```js
const Test = require('@codewars/test-compat');

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Invert array values",() => {
  const norm = arr => arr.map(n => n === -0 ? 0 : n);
  it("Basic Tests", () => {
    assert.deepEqual(norm(invert([1,2,3,4,5])), [-1,-2,-3,-4,-5]);
    assert.deepEqual(norm(invert([1,-2,3,-4,5])), [-1,2,-3,4,-5]);
    assert.deepEqual(norm(invert([])), []);
    assert.deepEqual(norm(invert([0])), [0]);
  });
});
```

---
## Code Solution

```js
function invert(arr) {
   return arr.map(n => -n)
}
```

---
## Resources I used for help

https://stackoverflow.com/questions/10168034/how-can-i-reverse-an-array-in-javascript-without-using-libraries

https://www.w3schools.com/jsref/jsref_reverse.asp

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse

https://forum.freecodecamp.org/t/negative-numbers-in-the-arrays/392177

https://josephcardillo.medium.com/how-to-reverse-arrays-in-javascript-without-using-reverse-ae995904efbe

---