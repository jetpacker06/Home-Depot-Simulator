import os
import time
import save
import main_hud
import logger

def inventory(s):
  woodPrice = 3
  screwsPrice = 1
  pipePrice = 2
  dont_break = True
  while dont_break:
    wood = save.getData("wood", s)
    screws = save.getData("screws", s)
    pvc_pipes = save.getData("pvc_pipes", s)
    balance = str(save.getData("balance", s))
    stock = [wood, screws, pvc_pipes]
    os.system('clear')
    print(" Wood:      ", stock[0], "\n Screws:    ", stock[1], "\n PVC Pipes: ", stock[2],  "\n Balance:    " + balance)
    options = input("What would you like to do?\n1. Purchase stocks\n2. Exit to main screen\n")
    if options == "1" :
      print("What do you want to buy?\n")
      pick = input("1. Wood: $3\n2. Screws: $1\n3. PVC pipes: $2\n")
      #handle wood
      if pick == "1":
        while True:
          amount = input("How much wood do you want to buy?\n")
          if amount.isnumeric():
            amount = int(amount)
          else:
            print("Enter a number!")
            continue
          if amount == 0:
            print("You didn't buy any.")
            break
          if (type(amount) == type(0)) & (amount > 0) & (save.getData("balance", s) - (amount * woodPrice) >= 0):
            save.saveData("wood", save.getData("wood", s) + amount, s)
            save.saveData("balance", save.getData("balance", s) - (amount * woodPrice), s)
            print("Successfully purchased " + str(amount) + " wood.")
            print("Your balance is now $" + str(save.getData("balance", s)) + ".")
            input("Press enter to continue.\n")
            break
          elif type(amount) != type(0):
            print("Type of amount")
            print(type(amount))
            print("Invalid amount!")
          elif amount <= 0:
            print("You must purchase at least 1!")
          elif save.getData("balance", s) - (amount * woodPrice) <= 0:
            print("You can't afford that many!")

      #handle screws
      elif pick == "2":
        while True:
          amount = input("How many screws do you want to buy?\n")
          if amount.isnumeric():
            amount = int(amount)
          else:
            print("Enter a number!")
            continue
          if amount == 0:
            print("You didn't buy any.")
            break
          if (type(amount) == type(0)) & (amount > 0) & (save.getData("balance", s) - (amount * screwsPrice) >= 0):
            save.saveData("screws", save.getData("screws", s) + amount, s)
            save.saveData("balance", save.getData("balance", s) - (amount * screwsPrice), s)
            print("Successfully purchased " + str(amount) + " screws.")
            print("Your balance is now $" + str(save.getData("balance", s)) + ".")
            input("Press enter to continue.\n")
            break
          elif type(amount) != type(0):
            print("Type of amount")
            print(type(amount))
            print("Invalid amount!")
          elif amount <= 0:
            print("You must purchase at least 1!")
          elif save.getData("balance", s) - (amount * woodPrice) <= 0:
            print("You can't afford that many!")
      #handle pvc pipes
      elif pick == "3":
        while True:
          amount = input("How many PVC pipes do you want to buy?\n")
          if amount.isnumeric():
            amount = int(amount)
          else:
            print("Enter a number!")
            continue
          if amount == 0:
            print("You didn't buy any.")
            break
          if (type(amount) == type(0)) & (amount > 0) & (save.getData("balance", s) - (amount * pipePrice) >= 0):
            save.saveData("pvc_pipes", save.getData("pvc_pipes", s) + amount, s)
            save.saveData("balance", save.getData("balance", s) - (amount * pipePrice), s)
            print("Successfully purchased " + str(amount) + " PVC Pipes.")
            print("Your balance is now $" + str(save.getData("balance", s)) + ".")
            input("Press enter to continue.\n")
            break
          elif type(amount) != type(0):
            print("Type of amount")
            print(type(amount))
            print("Invalid amount!")
          elif amount <= 0:
            print("You must purchase at least 1!")
          elif save.getData("balance", s) - (amount * woodPrice) <= 0:
            print("You can't afford that many!")
          
      else:
        input("Invalid input!")
        
    if options == "2" :
      dont_break = False
def inventoryFirstTime(s):
  woodPrice = 3
  dont_break = True
  while dont_break:
    wood = save.getData("wood", s)
    screws = save.getData("screws", s)
    pvc_pipes = save.getData("pvc_pipes", s)
    balance = str(save.getData("balance", s))
    stock = [wood, screws, pvc_pipes]
    os.system('clear')
    print(" Wood:      ", stock[0], "\n Screws:    ", stock[1], "\n PVC Pipes: ", stock[2],  "\n Balance:    " + balance)
    print("You have no items to sell. Let's fix that.")
    print("Start by buying some wood.")
    shouldRepeat = True
    while shouldRepeat:
      amount = input("How much wood do you want to buy?\n")
      if amount.isnumeric():
        amount = int(amount)
      else:
        print("Enter a number!")
        continue
      if amount == 0:
        print("Buy at least 1!")
        continue
      if (type(amount) == type(0)) & (amount > 0) & (save.getData("balance", s) - (amount * woodPrice) >= 0):
        save.saveData("wood", save.getData("wood", s) + amount, s)
        save.saveData("balance", save.getData("balance", s) - (amount * woodPrice), s)
        print("Successfully purchased " + str(amount) + " wood.")
        print("Your balance is now $" + str(save.getData("balance", s)) + ".")
        input("Press enter to continue.\n")
        shouldRepeat = False
        dont_break = False
      elif save.getData("balance", s) - (amount * woodPrice) <= 0:
        print("You can't afford that many!")
  print("Congratulations on your first purchase. Now you are free. To the main menu! Press Enter.")
  input()
  main_hud.open(s)