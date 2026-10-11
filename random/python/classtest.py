class computers:
  def __init__(self, name, price, company):
    self.name = name
    self.price = price
    self.company = company

  def nameMessage(self):
    return f"{self.name} says Hello World!"

  def priceMessage(self):
    return f"A {self.name} is ${self.price}"

  def companyMessage(self):
    return f"A {self.name} is made by {self.company}"

computer1 = computers("Chromebook", 100, "Google")
computer2 = computers("MacBook", 3000, "Apple")

print(computer1.name) 
print(computer1.price)
print(computer1.nameMessage()) 
print(computer1.priceMessage())
print(computer1.companyMessage())

print(computer2.name) 
print(computer2.price)
print(computer2.nameMessage()) 
print(computer2.priceMessage())
print(computer2.companyMessage())
