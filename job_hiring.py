import os
import json
import time
hired_list = ["Jeff", "Mark", "Barbara", "Jimothy", "Margaret", "Vanessa", "Roland", "Clarence", "Loretta"]
def hire():
  os.system('clear')
  print("Now, you can't run an establishment all on your own.")
  time.sleep(1)
  print("You'll need to hire workers to do the work that you don't want to do yourself.")
  time.sleep(2)
  print("However, our market requires the best of the best to keep our prices high and our lawsuits low.")
  time.sleep(3)
  print("Your wonderful and generous CEO has given you a select list of loyal elderly workers to exploit to their final moments.")
  time.sleep(2)
  print("Choose the correct worker for the jobs you want them to do.")
  time.sleep(3)
  print("Or don't.")
  time.sleep(2)
  print("Their lives are in your hands.")
  time.sleep(2)
  input()
  print(hired_list)
  os.system('clear')
  input_ask = input("Would you like to hire employees?")
  while True:
    input_hire = input("Which candidates would you like to hire?\n")
    hired_list.append(input_hire)
    print(hired_list)
    input()
    print("Would you like to hire more candidates?\n")
    input1 = input("y/n")
    if input1 == "y":
      continue
    else:
      break
