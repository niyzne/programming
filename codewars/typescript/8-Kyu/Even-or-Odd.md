# Even or Odd

---
## Info
	
Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Fundamentals | Mathematics

---
## Code

Solution

```ts
export function evenOrOdd(n:number):string {
  return "";
}
```

Sample Tests

```ts
import { evenOrOdd } from "./solution";
import { assert    } from "chai";

describe("Example tests", function() {
  it("evenOrOdd(1) should return 'Odd'", function(){
    assert.equal(evenOrOdd(1), "Odd");
  });
  it("evenOrOdd(2) should return 'Even'", function(){
    assert.equal(evenOrOdd(2), "Even");
  });
  it("evenOrOdd(-1) should return 'Odd'", function(){
    assert.equal(evenOrOdd(-1), "Odd");
  });
  it("evenOrOdd(-2) should return 'Even'", function(){
    assert.equal(evenOrOdd(-2), "Even");
  });
  it("evenOrOdd(0) should return 'Even'", function(){
    assert.equal(evenOrOdd(0), "Even");
  });
});
```

---
## Code Solution

```ts
export function evenOrOdd(n:number):string {
  if (n % 2 == 0) { return 'Even'; }
  return 'Odd';
}
```

---