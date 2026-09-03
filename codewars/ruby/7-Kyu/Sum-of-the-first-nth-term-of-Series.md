# Sum of the first nth term of Series

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

```ruby
def series_sum(n)
  # Happy Coding ^_^
    return ''
end
```

Sample Tests

```ruby
describe "Solution" do
  it "sample tests" do
    do_test( 0, "0.00")
    do_test( 1, "1.00")
    do_test( 2, "1.25")
    do_test( 3, "1.39")
    do_test( 4, "1.49")
    do_test( 5, "1.57")
    do_test( 6, "1.63")
    do_test( 7, "1.68")
    do_test( 8, "1.73")
    do_test( 9, "1.77")
    do_test(15, "1.94")
    do_test(39, "2.26")
    do_test(58, "2.40")
  end

    def do_test(n, expected)
        actual = series_sum(n)
        message = "n = #{n}\nexpected #{expected.inspect}\n" +
            "actual = #{actual.inspect}"
        expect(actual).to eq(expected), message
    end
end
```

---
## Code Solution

```ruby
def series_sum(n)
  newNum = 0
  for i in 0...n do
    a = 1 / (1 + 3 * i.to_f)
    newNum += a
  end
  return format("%.2f", newNum)
end
```

---
## Resources I used for help

https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-ruby

https://www.rubyguides.com/ruby-tutorial/ruby-if-else/

https://www.geeksforgeeks.org/ruby/ruby-loops-for-while-do-while-until/

https://www.rubyguides.com/ruby-tutorial/loops/

---