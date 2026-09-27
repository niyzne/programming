## Pythagorean Theorem (hypotenuse form)

---

$$
a^2 + b^2 = c^2
\quad\text{or}\quad
c = \sqrt{a^2 + b^2}
$$

---

### Python

```python
import math

def hypotenuse(a, b):
    return math.sqrt((a ** 2) + (b ** 2)) 
```

### R

```R
hypotenuse <- function(a, b) {
    sqrt((a ^ 2) + (b ^ 2))
}
```
