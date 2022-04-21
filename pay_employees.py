import random
import save
import os
def pay(s):
  print("\nTime to pay your workers!\n")
  while True:
    input_pay = input("How much do you want to pay your employees for the hour? Minimun $7/hr. \n")
    if int(input_pay) >= 7:
      hour_pay = int(input_pay) * random.randint(5, 8)
      payroll = len(save.getData("hired_list", s)) * hour_pay
      if save.getData("balance", s) - payroll <= 0:
        print("You've gone BANKRUPT!!!! It's game over for you...")
        save.saveData("bankrupt", True, s)
      else:
        print("You spent $", payroll, "on your employees!")
        input()
        os.system('clear')
        bal = save.getData("balance", s)
        save.saveData("balance", bal - payroll, s)
        save.saveData("daysUntilEmployeePayday", "14", s)
        break
    else:
      print("You have to pay your employees at least $7 an hour.\n")
      input()
      os.system('clear')
      continue