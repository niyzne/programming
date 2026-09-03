# Employee Profile Generator (Workshop)

## Code

```python
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

address = '123 Main Street'
address += ', Apartment 4B'

employee_age = 28

experience_years = 5
position = 'Data Analyst'
salary = 75000

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]

employee_info = full_name + ' is ' + str(employee_age) + ' years old'
experience_info = 'Experience: ' + str(experience_years) + ' years'
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'

print(experience_info)
print()
print(employee_card)
print()
print(department)
print(year_code)
print(initials)
print(last_three)
```

## Output

```
Experience: 5 years

Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000

DEV
2026
JD
001
```

---
