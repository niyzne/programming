# Volume of a Cuboid

---
## Info

Bob needs a fast way to calculate the volume of a [rectangular cuboid](https://en.wikipedia.org/wiki/Rectangular_cuboid) with three values: the `length`, `width` and `height` of the cuboid.

Write a function to help Bob with this calculation.

---
Geometry | Fundamentals | Mathematics

---
## Code

Solution

```ts
export function getVolumeOfCuboid(length: number, width:number, height:number): number {
   // Your code here
  return 0;
}
```

Sample Tests

```ts
import solution = require('./solution');
import {assert} from "chai";

describe("Some testing", function() {
  
  it("Sample tests", function() {
    assert.equal(solution.getVolumeOfCuboid(1,2,2), 4);    
    assert.equal(solution.getVolumeOfCuboid(6.3,2,5), 63);    
    assert.equal(solution.getVolumeOfCuboid(1,1,1), 1);  
    assert.equal(solution.getVolumeOfCuboid(52,17,5), 4420);  
  });
});
```

---
## Code Solution

```ts
export function getVolumeOfCuboid(l: number, w:number, h:number): number {
  return l * w * h
}
```

---