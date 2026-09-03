# Keep up the hoop

---
## Info

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (`n`) how many times the hoop goes round and it will return him an encouraging message:

- If Alex gets 10 or more hoops, return the string `"Great, now move on to tricks"`.
- If he doesn't get 10 hoops, return the string `"Keep at it until you get it"`.

---
Fundamentals

---
## Code

Solution

```ts
export function hoopCount(n: number): string {
  //your code here
}
```

Sample Tests

```ts
import { assert } from "chai";

import {hoopCount} from "./solution";

describe("Keep up the hoop", () => {
  it("Fixed tests", () => {
    assert.strictEqual(hoopCount(6), "Keep at it until you get it");
    assert.strictEqual(hoopCount(10), "Great, now move on to tricks");
    assert.strictEqual(hoopCount(22), "Great, now move on to tricks");
  });
});
```

---
## Code Solution

```ts
export function hoopCount(n: number): string {
  if (n >= 10) { return 'Great, now move on to tricks' }
  return 'Keep at it until you get it'
}
```

---