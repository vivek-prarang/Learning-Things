class Car:
  def __init__(self, model,price,company):
    self.model=model
    self.price=price
    self.company=company

  def get_car_info(self):
    return f'{self.model} is related to {self.company} with {self.price}.'


car1=Car("Nano","1.5L","Tata")

print(car1.get_car_info())
