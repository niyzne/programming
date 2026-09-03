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

```shell
#!/bin/bash
length=$1
width=$2
height=$3
```

Sample Tests

```shell
test1 = run_shell args: ['2','5', '6']
test2 = run_shell args: ['6.3','3', '5']

describe "exampleTests" do
   it "should return the product" do
     expect(test1).to include('60')
     expect(test2).to include('94.5')
end
end
```

---
## Code Solution

```shell
#!/bin/bash
l=$1
w=$2
h=$3

echo "$l * $w * $h" | bc
```

---