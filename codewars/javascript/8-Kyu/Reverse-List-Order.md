# Reverse List Order

---
## Info

In this kata you will create a function that takes in a list and returns a list with the reverse order.

### Examples (Input -> Output)

```
* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9]
```

---
Lists | Fundamentals

---
## Code

Solution

```js
function reverseList(list) {

}
```

Sample Tests

```js
const Test = require('@codewars/test-compat');

describe("reverseList", function(){
  it("should reverse some sample arrays", function(){
    Test.assertSimilar(reverseList([1,2,3,4]), [4,3,2,1]);
    Test.assertSimilar(reverseList([3,1,5,4]), [4,5,1,3]);
  });
});
```

---
## Code Solution

```js
function reverseList(l) {
  return l.reverse();
}
```

---
## Resources I used for help

https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/javascript

---