# Remove exclamation marks

---
## Info

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

---
Fundamentals | Strings

---
## Code

Solution

```js
function removeExclamationMarks(s) {
  return '';
}
```

Sample Tests

```js
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(removeExclamationMarks("Hello World!"), "Hello World");
  });
});
```

---
## Code Solution

```js
function removeExclamationMarks(s) {
  return s.replace(/!/g, "")
}
```

---