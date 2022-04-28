import json
import random
import os
import save
import job_hiring
import inventory
import minigame
import pay_employees
import end_day


def open(s):
  dontQuit = True
  while dontQuit:
    os.system('clear')
    print("---Main Menu---\n")
    print("Your balance is: $" + str(save.getData("balance", s))) 
    #print("Profit: $", profit)
    print("Employee payday is in " + str(save.getData("daysUntilEmployeePayday", s)) + " days.")
    print("\nWhat would you like to do?\n1. View hired employees.\n2. Hire employees\n3. Fire employees\n4. Purchase items to sell\n5. End the day\n6. Quit the program.")
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
    if action == "4":
      inventory.inventory(s)
    if action == "5":
      end_day.dayOverview(s)
      end_day.end_day(s)
    if action == "6":
      os.system("clear")
      print("Later.")
      dontQuit = False
    if save.getData("balance", s) <= 0 & save.getData("bankrupt", s) == False:
        input("Uh oh!!! you don't have any money left!!\n Try your best to make a profit by next payday or you're bankrupt!!\n\nPress enter to continue")