# Sum of the first nth term of Series


---
#CodeWars #php #code #coding #programming #7Kyu

---
## Task

Your task is to write a function which returns the `n`-th term of the following series, which is the sum of the first `n` terms of the sequence (`n` is the input parameter).

Series:1+14+17+110+113+116+…\mathrm{Series:}\quad 1 + \frac14 + \frac17 + \frac1{10} + \frac1{13} + \frac1{16} + \dotsSeries:1+41​+71​+101​+131​+161​+…

You will need to figure out the rule of the series to complete this.
## Rules

- You need to round the answer to 2 decimal places and return it as String.
- If the given value is `0` then it should return `"0.00"`.
- You will only be given Natural Numbers as arguments.
## Examples (Input --> Output)

```
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
```

---
Fundamentals

---
## Code

Solution

```php
<?php
  
function series_sum(int $n): string {
  return '0.00'; // Your code here
}
```

Sample Tests

```php
<?php
use PHPUnit\Framework\TestCase;

class SeriesSumTest extends TestCase {
  
    private function doTest(int $n, string $expected) {
        $this->assertSame($expected, series_sum($n), "series_sum($n) returned an incorrect answer.");
    }

    public function testExamples() {
        $this->doTest(0, '0.00');
        $this->doTest(1, '1.00');
        $this->doTest(2, '1.25');
        $this->doTest(3, '1.39');
        $this->doTest(4, '1.49');
    }
}
```

---
## Code Solution

```php
<?php
  
function series_sum(int $n): string {
  $newNum = 0;

  for ($i = 0; $i < $n; $i++) {
      $a = 1 / (1 + 3 * $i);
      $newNum += $a;
  }
  return sprintf("%.2f", $newNum);
}
```

---