import random
import save
import os
def pay(s):
  dayend = input("Are you sure you want to end the day? y/n\n")
  if dayend == ("y"):
    days = save.getData("daysUntilEmployeePayday", s)
    days = int(days) - 1
    save.saveData("daysUntilEmployeePayday", days, s)
  if save.getData("daysUntilEmployeePayday", s) == 0:
    print("\nTime to pay your workers!\n")
    while True:
      input_pay = input("How much do you want to pay your employees for the hour? ")
      if int(input_pay) >= 7:
        hour_pay = int(input_pay) * random.randint(5, 8)
        payroll = len(save.getData("hired_list", s)) * hour_pay
        if save.getData("balance", s) - payroll <= 0:
          print("You've gone BANKRUPT!!!! It's game over for you...")
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