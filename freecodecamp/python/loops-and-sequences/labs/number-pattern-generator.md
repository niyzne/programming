# Number Pattern Generator (lab)

## Code

```python
def number_pattern(n):
	result = []
	if isinstance(n, int):
		if n < 1:
			return 'Argument must be an integer greater than 0.'
		else:
			for num in range(1, n+1):
				result.append(str(num))
			return " ".join(result)
	else:
		return 'Argument must be an integer value.'

print(number_pattern(4))
```

## Output

```
1 2 3 4
```

---