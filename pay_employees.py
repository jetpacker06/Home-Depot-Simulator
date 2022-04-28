import random
import save
import os
def pay(s):
  if len(save.getData("hired_list", s)) != 0:
    print("\nTime to pay your workers!\n")
    input_pay = input("How much do you want to pay your employees for the hour? Minimum $7/hr. \n")
    while True:
      if input_pay.isnumeric():
        if int(input_pay) >= 7:
          input_pay = int(input_pay)
          break
        else:
           print("Must pay $7 per hour or more.")
      else:
        print("Must be a number.")
      input_pay = input("How much do you want to pay your employees for the hour?\n")
  
    hour_pay = int(input_pay) * random.randint(5, 8)
    payroll = len(save.getData("hired_list", s)) * hour_pay
    if save.getData("balance", s) - payroll <= 0:
      print("You've gone BANKRUPT!!!! It's game over for you...")
      save.saveData("bankrupt", True, s)
      
    else:
      print("You spent $", payroll, "on your employees!")
      input("Press Enter to continue.\n")
      os.system('clear')
      bal = save.getData("balance", s)
      save.saveData("balance", bal - payroll, s)
      save.saveData("daysUntilEmployeePayday", 14, s)
  else:
    print("You have no employees to pay!")
    input("\nPress enter to continue.\n")