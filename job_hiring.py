import os
import time
import save
import main_hud
import logger
import inventory

def job_hire_first_time(s):
  #0 to skip sequence or else 1
  multiplier_for_skip = 1
  time.sleep(1 * multiplier_for_skip)
  print("You'll need to hire workers to do the work that you don't want to do yourself.")
  time.sleep(2 * multiplier_for_skip)
  print("However, our market requires the best of the best to keep our prices high and our lawsuits   low.")
  time.sleep(3 * multiplier_for_skip)
  print("Your wonderful and generous CEO has given you a select list of loyal elderly workers to exploit to their final moments.")
  time.sleep(2 * multiplier_for_skip)
  print("Choose the correct worker for the jobs you want them to do.")
  time.sleep(3 * multiplier_for_skip)
  print("Or don't.")
  time.sleep(2 * multiplier_for_skip)
  print("Their lives are in your possibly capable hands!")
  time.sleep(2 * multiplier_for_skip)
  
  
  if len(save.getData("unhired_list", s)) == 0:
    input("You have hired enough workers, you can't hire more!\n")
  else:
    input_ask = input("Would you like to hire employees?\ny/n\n")
    if input_ask.lower() == "y":
      os.system("clear")
      shouldContinue = True
      while shouldContinue:
        print("\nHere are your options.")
        #loop to print all non-hired employees
        i = 0
        while i < len(save.getData("unhired_list", s)):
          print(save.getData("unhired_list", s)[i])
          i += 1
        print("Enter the name of the candidate would like to hire.\n")
        selected_hire = input()
        hiredArr = save.getData("hired_list", s)
        if type(hiredArr) == type(None):
          hiredArr = []
        unhiredArr = save.getData("unhired_list", s)
        selected_hire = selected_hire.capitalize()
       
        if selected_hire in unhiredArr:
          unhiredArr.remove(selected_hire)
          hiredArr.append(selected_hire)
          save.saveData("hired_list", hiredArr, s)
          save.saveData("unhired_list", unhiredArr, s)
        else:
          print("Not in hirable list!")
        print("Would you like to hire more candidates?\n")
        input1 = input("y/n\n")
        if input1.lower() == "y":
          continue
        else:
          shouldContinue = False
  print("Next, we recommend buying some inventory. A balance of products creates the most profit!")
  input("Press Enter to continue.\n")
  inventory.inventoryFirstTime(s)
def job_hire(s):
  if len(save.getData("unhired_list", s)) == 0:
    input("You have hired enough workers, you can't hire more!\n")
  else:
    os.system('clear')
    input_ask = input("Would you like to hire employees?\ny/n\n")
    if input_ask.lower() == "y":
      while True:
        print("\nHere are your options.")
        #loop to print all non-hired employees
        i = 0
        while i < len(save.getData("unhired_list", s)):
          print(save.getData("unhired_list", s)[i])
          i += 1
        print("Enter the name of the candidate would like to hire.\n")
        selected_hire = input()
        hiredArr = save.getData("hired_list", s)
        if type(hiredArr) == type(None):
          hiredArr = []
        unhiredArr = save.getData("unhired_list", s)
        selected_hire = selected_hire.capitalize()
       
        if selected_hire in unhiredArr:
          unhiredArr.remove(selected_hire)
          hiredArr.append(selected_hire)
          save.saveData("hired_list", hiredArr, s)
          save.saveData("unhired_list", unhiredArr, s)
        print("Would you like to hire more candidates?\n")
        input1 = input("y/n\n")
        if input1.lower() == "y":
          continue
        else:
          main_hud.open(s)
    else:
      main_hud.open(s)
def job_fire(s):
  os.system('clear')
  input_ask = input("Would you like to fire employees?\ny/n\n")
  if input_ask.lower() == "y":
    while True:
      print("\nHere are your options.")
      #loop to print all hired employees
      i = 0
      while i < len(save.getData("hired_list", s)):
        print(save.getData("hired_list", s)[i])
        i += 1
      print("Enter the name of the candidate would like to fire.\n")
      selected_fire = input()
      hiredArr = save.getData("hired_list", s)
      if type(hiredArr) == type(None):
        hiredArr = []
      unhiredArr = save.getData("unhired_list", s)
      selected_fire = selected_fire.capitalize()
     
      if selected_fire in hiredArr:
        unhiredArr.append(selected_fire)
        hiredArr.remove(selected_fire)
        save.saveData("hired_list", hiredArr, s)
        save.saveData("unhired_list", unhiredArr, s)
      print("Would you like to fire more candidates?\n")
      input1 = input("y/n\n")
      if input1.lower() == "y":
        continue
      else:
        break
      main_hud.open(s)