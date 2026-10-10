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
