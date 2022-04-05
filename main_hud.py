import json
import random
import os
import save
#from job_hiring import hired_list

def open(s):
  while True:
    os.system('clear')
    print("---Main Menu---\n")
    print("Your balance is: " + save.getData("balance", s))
    print("Employee payday is in " + str() + " days.")
    print("\nWhat would you like to do?\n1.Hire employees")
    

def payroll(s):
  daysUntilPayday = 14
  os.system('clear')
  daysUntilPayday -= 1
  if daysUntilPayday == 0:
    print("Time to pay your employees!")
    input()
    input_pay = input("How much do you want to pay your employees for the hour?")
    hour_pay = int(input_pay) * random.randint(5, 8)
    payroll = len(save.getData("hired_list")) * hour_pay
    print("You spent", payroll, "on your employees!")
    daysUntilPayday = 14