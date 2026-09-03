# Grasshopper - Debug sayHello

---
## Info

## Debugging sayHello function

The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

Example output:

```
Hello, Mr. Spock
```

---
Fundamentals

---
## Code

Solution

```js
function sayHello(name) {
  return 'Hello'
}
```

Sample Tests

```js
const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(sayHello('Mr. Spock'), 'Hello, Mr. Spock')
    assert.strictEqual(sayHello('Captain Kirk'), 'Hello, Captain Kirk')
    assert.strictEqual(sayHello('Liutenant Uhura'), 'Hello, Liutenant Uhura')
    assert.strictEqual(sayHello('Dr. McCoy'), 'Hello, Dr. McCoy')
  });
});
```

---
## Code Solution

```js
function sayHello(name) {
  return `Hello, ${name}`
}
```

---
## Resources I used for help

https://www.geeksforgeeks.org/python/javascript-equivalent-of-python-f-string/

---