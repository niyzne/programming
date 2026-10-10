def yesFunction(a):
  if a == 1:
    return 1
  return 0

def notFunction(a):
  if a == 1:
    return 0
  return 1

def andFunction(a, b):
  if a and b:
    return 1
  return 0

def orFunction(a, b):
  if a or b:
    return 1
  return 0

def nandFunction(a, b):
  if a and b:
    return 0
  return 1

def norFunction(a, b):
  if a or b:
    return 0
  return 1

def xorFunction(a, b):
  if (a or b) and not ((a and b) or (not a and not b)):
    return 1
  return 0

def xnorFunction(a, b):
  if not ((a or b) and not ((a and b) or (not a and not b))):
    return 1
  return 0

# print("======")
# print(yesFunction(0))
# print(yesFunction(1))
#
# print("======")
# print(notFunction(0))
# print(notFunction(1))
#
# print("======")
# print(andFunction(0, 0))
# print(andFunction(0, 1))
# print(andFunction(1, 0))
# print(andFunction(1, 1))
#
# print("======")
# print(orFunction(0, 0))
# print(orFunction(0, 1))
# print(orFunction(1, 0))
# print(orFunction(1, 1))
#
# print("======")
# print(nandFunction(0, 0))
# print(nandFunction(0, 1))
# print(nandFunction(1, 0))
# print(nandFunction(1, 1))
#
# print("======")
# print(norFunction(0, 0))
# print(norFunction(0, 1))
# print(norFunction(1, 0))
# print(norFunction(1, 1))
#
# print("======")
# print(xorFunction(0, 0))
# print(xorFunction(0, 1))
# print(xorFunction(1, 0))
# print(xorFunction(1, 1))
#
# print("======")
# print(xnorFunction(0, 0))
# print(xnorFunction(0, 1))
# print(xnorFunction(1, 0))
# print(xnorFunction(1, 1))
