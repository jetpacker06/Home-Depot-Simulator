import json
import random
import os
import save
import job_hiring

def open(s):
  while True:
    os.system('clear')
    print("---Main Menu---\n")
    print("Your balance is: $" + str(save.getData("balance", s))) 
    #print("Profit: $", profit)
    print("Employee payday is in " + str(save.getData("daysUntilEmployeePayday", s)) + " days.")
    print("\nWhat would you like to do?\n1. View hired employees.\n2. Hire employees\n3. Fire employees\n4. \n5. Work & end the day")
    action = input()
    if action == "1":
      if len(save.getData("hired_list", s)) == 0:
        print("You haven't hired any employees! You probably should.")
      else:
        print("\nCurrently hired employees:\n")
        #loop to print all non-hired employees
        i = 0
        while i < len(save.getData("hired_list", s)):
          print(save.getData("hired_list", s)[i])
          i += 1
      input("Press enter.")
    if action == "2":
      job_hiring.job_hire(s)
    if action == "3":
      job_hiring.job_fire(s)
  #  if action = "4"
      
    if action == "5":
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
          print("You spent $", payroll, "on your employees!")
          input()
          os.system('clear')
          bal = save.getData("balance", s)
          save.saveData("balance", bal - payroll, s)
          save.saveData("daysUntilEmployeePayday", "14", s)
          break
        else:
          print("You have to pay your employees at least $7 an hour.")
          input()
          os.system('clear')
          continue
        