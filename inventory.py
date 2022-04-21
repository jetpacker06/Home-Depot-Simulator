import os
import time
import save
import main_hud
import logger

def inventory(s):
  woodPrice = 1
  screwsPrice = 1
  pipePrice = 1
  dont_break = True
  while dont_break:
    wood = save.getData("wood", s)
    screws = save.getData("screws", s)
    pvc_pipes = save.getData("pvp_pipes", s)
    balance = str(save.getData("balance", s))
    stock = [wood, screws, pvc_pipes]
    os.system('clear')
    print(" Wood:      ", stock[0], "\n Screws:    ", stock[1], "\n PVC Pipes: ", stock[2],  "\n Balance:    " + balance)
    options = input("What would you like to do?\n1. Purchase stocks\n2. Sell stock\n3. Exit to main screen\n")
    if options == "1" :
      print("Tier 1 options:\n1. Wood\n2. Screws\n3. PVC pipes\n")
      pick = input("What do you want to buy?\n")
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
            save.saveData("screws", save.getData("pcv_pipes", s) + amount, s)
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
          
      else:
        input("Invalid input!")
      
    if options == "2" : #I now feel like thinking about this
      stock_sold = input("What would you like to sell?\n1. Wood\n2. Screws\n3. PVC Pipes\n")
      if stock_sold.isnumeric():
        stock_sold = int(stock_sold)
      if stock_sold == "1":
        while True:
          amount_sold = input("How much wood do you want to sell?\n")
          if amount_sold.isnumeric():
            amount_sold = int(amount_sold)
          else:
            print("Enter a number!")
            continue
          if amount_sold == 0:
            print("You didn't buy any.")
            break
          if (type(amount_sold) == type(0)) & (amount_sold > 0) & (save.getData("balance", s) + (amount * woodPrice) >= 0):
            save.saveData("wood", save.getData("wood", s) + amount_sold, s)
            save.saveData("balance", save.getData("balance", s) - (amount_sold * woodPrice), s)
            print("Successfully sold " + str(amount_sold) + " wood.")
            print("Your balance is now $" + str(save.getData("balance", s)) + ".")
            input("Press enter to continue.\n")
            break
          elif type(amount_sold) != type(0):
            print("Type of amount")
            print(type(amount_sold))
            print("Invalid amount!")
          elif amount <= 0:
            print("You must purchase at least 1!")
          elif save.getData("balance", s) - (amount_sold * woodPrice) <= 0:
            print("You can't afford that many!")
    
    elif amount_sold == "2": 
      print("")
    
    elif amount_sold == "3":
      print("")
    
    if options == "3" :
      dont_break = False