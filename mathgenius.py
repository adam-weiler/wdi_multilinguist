import math #Needed to use math.factorial.

from multilinguist import Multilinguist #Needed to inherit Multilinguist class.

class MathGenius(Multilinguist):
  """The multilinguist documentation tells us that 
  class represents a world-traveller who speaks many 
  languages. The MathGenius class represents a 
  world-travelling math genius who can speak many 
  languages and mentally add up huge lists of numbers.
  """

  def report_total(self, numbers_list):
    """(Roughly) translates msg into current_lang using the Transltr API
    as well as finding the sum of the number_list."""
    return f"{self.say_in_local_language('The total is')} {sum(numbers_list)}"

  def factorial(self, number):
    """Calculates the factorial of the number given."""
    return f"{math.factorial(number)}"