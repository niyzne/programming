### If

You can use `if`, `elif` and `else` to run code conditionally.

```python
if condition1:
    do_a_flip()
elif condition2:
    harvest()
else:
    do_a_flip()
    harvest()
```

#### Syntax

`if`s allow you to run code only if some condition is `True`. They are like a `while` loop that doesn't loop.

The `if` takes a condition just like the `while` loop and executes the `if` code block if the condition evaluates to `True`:

```python
# do a flip if condition is True
if condition:
    do_a_flip()
```

You can also add an `else` after the `if` that defines code to be executed if the condition evaluates to `False`.

Do a flip if condition is True, otherwise harvest.

```python
if condition:
    do_a_flip()
else:
    harvest()
```

`elif` is short for `else if`.

```python
if condition1:
    # a
else:
    if condition2:
        # b
    else:
        # c
```

can be shortened to:

```python
if condition1:
    # a
elif condition2:
    # b
else:
    # c
