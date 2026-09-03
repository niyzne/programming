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

```ts
export function reverseList(list: number[]): number[] {
  return [];
}
```

Sample Tests

```ts
import { assert } from "chai";
import { reverseList } from "./solution";

describe("reverseList", function(){
  it("should reverse some sample arrays", function(){
    assert.deepEqual(reverseList([1,2,3,4]), [4,3,2,1], "Input=[1,2,3,4]");
    assert.deepEqual(reverseList([3,1,5,4]), [4,5,1,3], "Input=[3,1,5,4]");
  });
});
```

---
## Code Solution

```ts
export function reverseList(list: number[]): number[] { return list.reverse() }
```

---
## Resources I used for help

https://www.webdevtutor.net/blog/typescript-reverse-list

---