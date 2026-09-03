# Build an RPG Character (lab)

## Code

```python
full_dot = '●'
empty_dot = '○'

def validate_name(name):
	if not isinstance(name, str):
		return 'The character name should be a string'
	if name == '':
		return 'The character should have a name'
	if len(name) > 10:
		return 'The character name is too long'
	if ' ' in name:
		return 'The character name should not contain spaces'

def validate_stat(strength, intelligence, charisma):
	for stat in (strength, intelligence, charisma):
		if not isinstance(stat, int):
			return 'All stats should be integers'
		if stat < 1:
			return 'All stats should be no less than 1'
		if stat > 4:
			return 'All stats should be no more than 4'
	if (strength + intelligence + charisma) != 7:
		return 'The character should start with 7 points'

def create_dots(stat):
	return full_dot * stat + empty_dot * (10 - stat)

def create_character(name, strength, intelligence, charisma):

	name_error = validate_name(name)
	if name_error:
		return name_error

	stat_error = validate_stat(strength, intelligence, charisma)
	if stat_error:
		return stat_error

	return (
		f'{name}\n'
		f'STR {create_dots(strength)}\n'
		f'INT {create_dots(intelligence)}\n'
		f'CHA {create_dots(charisma)}'
	)

create_character('ren', 4, 2, 1)
```

## Output

N/A

---
