import random

def test(n):
  l = [0, 1, 2, 3, 4, 5]
  a = random.choice(l)

  while a != 5:
    print(f'hello {n}')
    a = random.choice(l)
  print(f'{n} died')

n = input("name: ")
test(n)
