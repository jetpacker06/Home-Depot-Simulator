import os
import random
import time
import save
import main_hud
hired_list = ["Jeff", "Mark", "Barbara", "Jimothy", "Margaret", "Vanessa", "Roland", "Clarence", "Loretta"]
#we should rework the employee lists to use save data, i say we add two saved objects: a default list and a hired list. each time you hire an employee, that employee name is moved from the first list to the second. if you fire them, they move back to the first.
def job_hire_first_time(s):
  #0 to skip sequence
  multiplier_for_skip = 0
  os.system('clear')
  print("Now, you can't run an establishment all on your own.")
  time.sleep(1 * multiplier_for_skip)
  print("You'll need to hire workers to do the work that you don't want to do yourself.")
  time.sleep(2 * multiplier_for_skip)
  print("However, our market requires the best of the best to keep our prices high and our lawsuits low.")
  time.sleep(3 * multiplier_for_skip)
  print("Your wonderful and generous CEO has given you a select list of loyal elderly workers to exploit to their final moments.")
  time.sleep(2 * multiplier_for_skip)
  print("Choose the correct worker for the jobs you want them to do.")
  time.sleep(3 * multiplier_for_skip)
  print("Or don't.")
  time.sleep(2 * multiplier_for_skip)
  print("Their lives are in your possibly capable hands!")
  time.sleep(2 * multiplier_for_skip)
  print("Press enter to continue.")
  time.sleep(2 * multiplier_for_skip)
  job_hire(s)

def job_hire(s):
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
      input_hire = input("Which candidates would you like to hire?\n")
      hired_list.append(input_hire)
      print(hired_list)
      print("Would you like to hire more candidates?\n")
      input1 = input("y/n")
      if input1.lower() == "y":
        continue
      else:
        break
  else:
    main_hud.open(s)
