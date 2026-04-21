class BasicFormula():
  def __init__(self) -> None:
    pass

  def _sum_of_numbers(self,num):
    # Base case
    if (num//10 ==0):
      return num
    return num % 10 + self._sum_of_numbers(num // 10)

  def _separate_each_digits(self,num):
    if (num//10 ==0):
       return [num]
    return self._separate_each_digits(num // 10)+[num % 10]

  def _sum_of_numbers_to_single(self,num):
  # Base Case
    if num < 10:
      return num
    return self._sum_of_numbers_to_single(self._sum_of_numbers(num))
  def _place_value(self,list):
    return [i for i in list]
