# ===============
# == No ai btw ==
# ===============

age = int(input('What is your age?: '))
funny = age - 67

print(f'your age is {age}')
print('congratulations!')

for n in range(1, (age * age) + 1):
    print(n)

print(f'your funny number is {funny}')

password = input('type the right password: ')

# (hint, the password might be 676767, or might not be, idk)
while password != '676767':
    print('WRONG!')
    print('try again')
    password = input('password: ')
print('NICE!')

print('lets continue!')

def greet(n):
    print(f'Hello {n}')

name = str(input('what is your name?: '))
greet(name)

print('okay okay')
print('lets try something more')
print('I N T E R E S T I N G')
print('hahahaha')

def mult(a, b):
    print(f'wow, printing {a} + {b} = {a * b}')

print('good at math?')
print('no?')
print("no worries! we'll help!")
print("we'll start with multiplication")
print('select two numbers you want to multiply')

numa = int(input('number a: '))
numb = int(input('number b: '))
mult(numa, numb)

print('nice')

print('so... you want more calculations?')
print('how about you get a job instead of doing this')
print('alr that was a bit mean, lets continue lol')
# yeah mb maybe was a bit mean lol
