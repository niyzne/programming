# Parse nice int from char problem

---
## Info

## Build Tower

You ask a small girl "How old are you?" She always says "x years old", where `x` is a random number between `0` and `9`.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

---
Fundamentals

---
## Code

Solution

```js
function getAge(inputString){
// return the girl's correct age as an integer. Happy coding :) 
}
```

Sample Tests

```js
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests",() =>{
  it("Testing for fixed tests", () => {
    assert.strictEqual(getAge("4 years old"), 4);
    assert.strictEqual(getAge("9 years old"), 9);
    assert.strictEqual(getAge("1 year old"), 1);    
  })
})
```

---
## Code Solution

```js
function getAge(inputString) {
    let matches = inputString.match(/(\d+)/);
    if (matches) { return Number(matches[0]); } 
}
```

---
## Resources I used for help

https://www.geeksforgeeks.org/javascript/extract-a-number-from-a-string-using-javascript/

https://stackoverflow.com/questions/10003683/how-can-i-extract-a-number-from-a-string-in-javascript

https://www.w3schools.com/JSREF/jsref_parseint.asp

---
