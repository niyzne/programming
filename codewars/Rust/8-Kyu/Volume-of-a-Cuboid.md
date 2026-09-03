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

```rust
fn get_volume_of_cuboid(length: f32, width: f32, height: f32) -> f32 {
    // your code here
}
```

Sample Tests

```rust
// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(get_volume_of_cuboid(1.0, 2.0, 2.0), 4.0);
        assert_eq!(get_volume_of_cuboid(6.3, 2.0, 5.0), 63.0);
    }
}
```

---
## Code Solution

```rust
fn get_volume_of_cuboid(l: f32, w: f32, h: f32) -> f32 { l * w * h }
```

---