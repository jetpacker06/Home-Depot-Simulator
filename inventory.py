import os
import time
import save
import main_hud
import logger

def inventory(s):
  dont_break = True
  while dont_break:
    wood = save.getData("wood", s)
    screws = save.getData("screws", s)
    pvc_pipes = save.getData("pvp_pipes", s)
    stock = [wood, screws, pvc_pipes]
    os.system('clear')
    print(" Wood:      ", stock[0], "\n Screws:    ", stock[1], "\n PVC Pipes: ", stock[2])
    options = input("What would you like to do?\n1. Purchase stocks\n2. Sell stock\n3. Exit to main screen\n")
    if options == "1" :
      input("TBD")
    if options == "2" :
      input("TBD")
    if options == "3" :
      dont_break = False

