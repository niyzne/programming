# Remove anchor from URL

---
Complete the function/method so that it returns the url with anything after the anchor (`#`) removed.

## Examples

```
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
```

---
Regular Expressions | Strings | Fundamentals

---
## Code

Solution

```js
function removeUrlAnchor(url){
  // TODO: complete
}
```

Sample Tests

```js
const { assert } = require("chai")

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(removeUrlAnchor('www.codewars.com#about'), 'www.codewars.com')
    assert.strictEqual(removeUrlAnchor('www.codewars.com/katas/?page=1#about'), 'www.codewars.com/katas/?page=1')
    assert.strictEqual(removeUrlAnchor('www.codewars.com/katas/'), 'www.codewars.com/katas/')
    })
  })
```

---
## Code Solution

```js
function removeUrlAnchor(url){ return url.split('#')[0] }
```

---