# Even or Odd

---
## Info

Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.

---
Fundamentals | Mathematics

---
## Code

Solution

```rust
fn even_or_odd(number: i32) -> &'static str {
    todo!()
}
```

Sample Tests

```rust
// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod sample_tests {
    use super::even_or_odd;
    
    fn do_test(number: i32, expected: &str) {
        let actual = even_or_odd(number);
        assert_eq!(actual, expected, "\nYour result (left) does not match the expected output (right) for the input {number:?}");
    }

    #[test]
    fn test_zero() {
        do_test(0, "Even");
    }

    #[test]
    fn test_positive_even() {
        do_test(2, "Even");
    }

    #[test]
    fn test_positive_odd() {
        do_test(1, "Odd");
    }

    #[test]
    fn test_negative_even() {
        do_test(-2, "Even");
    }

    #[test]
    fn test_negative_odd() {
        do_test(-1, "Odd");
    }
}
```

---
## Code Solution

```rust
fn even_or_odd(num: i32) -> &'static str {
    if num % 2 == 0 { "Even" } else { "Odd" }
}
```

---