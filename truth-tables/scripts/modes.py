import truthTables

def addition(a, b):
  if a or b:
    return 1
  return 0

def multiplication(a, b):
  if a and b:
    return 1
  return 0







def andFunction(a, b):
  if a and b:
    return 1
  return 0

def orFunction(a, b):
  if a or b:
    return 1
  return 0

a = andFunction(0, 1)
b = orFunction(1, 1)
print(a)
print(b)

print(addition(a, b))
print(multiplication(a, b))
