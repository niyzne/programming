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

```ts
export function invert(array: number[]): number[] {
   return [];
}
```

Sample Tests

```ts
// See https://www.chaijs.com for how to use Chai.
import { assert } from "chai";

import { invert } from "./solution";

// TODO Add your tests here
describe("Invert array values", function() {
  it("Basic Tests", function(){
    assert.deepEqual(invert([1,2,3,4,5]), [-1,-2,-3,-4,-5]);
    assert.deepEqual(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5]);
    assert.deepEqual(invert([]), []);
    assert.deepEqual(invert([0]), [-0]);
  });
});
```

---
## Code Solution

```ts
export function invert(arr: number[]): number[] {
   return arr.map(n => -n)
}
```

---
## Resources I used for help

https://www.geeksforgeeks.org/typescript/typescript-array-reverse-method/

https://stackoverflow.com/questions/46763647/how-to-reverse-the-array-in-typescript-for-the-following-data

https://www.geeksforgeeks.org/typescript/typescript-array-reverse-method/

https://www.spguides.com/how-to-reverse-an-array-in-typescript-array-reverse-method/

https://stackoverflow.com/questions/46763647/how-to-reverse-the-array-in-typescript-for-the-following-data

---