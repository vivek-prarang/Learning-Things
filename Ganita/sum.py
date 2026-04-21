from basic import BasicFormula

class Sum(BasicFormula):
  def __init__(self) -> None:
    super().__init__()

  def sum_of_two_numbers(self,num1,num2):
    return num1+num2

  def sum_of_n_numbers(self,nums):
    return self._separate_each_digits(nums[0])



sum=Sum()
s=sum.sum_of_n_numbers([123])


print(s)
