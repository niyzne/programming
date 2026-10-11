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
