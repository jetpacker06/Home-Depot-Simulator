import save
import minigame
import random
import pay_employees
def end_day(s):
  #play minigame, calculate earnings, pay employees if it is time
  minigame.play(s)
  #calculate earnings for day
  save.saveData("daysUntilEmployeePayday", save.getData("daysUntilEmployeePayday", s) - 1, s)
  if save.getData("daysUntilEmployeePayday", s) == 0:
    pay_employees.pay(s)