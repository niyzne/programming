# User Configuration Manager (Certification Project)

## Code 

```python
test_settings = {
	'Theme': 'dark',
	'Volume': 'high'
}

def add_setting(dictionary, pair):
	key, value = pair
	key = key.lower()
	value = value.lower()
	
	if key in dictionary:
		return f"Setting '{key}' already exists! Cannot add a new setting with this name."
	dictionary[key] = value
	return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, pair):
	key, value = pair
	key = key.lower()
	value = value.lower()
	
	if key in dictionary:
		dictionary[key] = value
		return f"Setting '{key}' updated to '{value}' successfully!"
	return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key):
	key = key.lower()
	
	if key in dictionary:
		del dictionary[key]
		return f"Setting '{key}' deleted successfully!"
	return 'Setting not found!'

def view_settings(settings):
	if not settings:
		return 'No settings available.'
	message = "Current User Settings:\n"
	for key, value in settings.items():
		formatted_line = key.capitalize() + ": " + value
		message += f'{formatted_line}\n'
	return message
```

## Output

```
N/A
```

---