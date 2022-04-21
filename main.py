import json
import intro_sequence
import time
import save
import get_saves_count
import os
import logger
import main_hud

def newSave():
  #new save
  #request new name, create new save, create name of new save, move on to intro
  
  new_save_name = input("Enter the name of your new save.\n")
  saves = open("saves.json", "r")
  saves_dict = json.loads(saves.read())
  saves.close()
  s = "save" + str(get_saves_count.getSavesCount())
  saves_dict[s] = {}
  saves = open("saves.json", "w")
  saves.write(json.dumps(saves_dict))
  saves.close()

  save.saveData("name", new_save_name, s)
  save.saveData("balance", 1000, s)
  save.saveData("unhired_list", ["Jeff", "Mark", "Barbara", "Jimothy", "Margaret", "Vanessa", "Roland", "Clarence", "Loretta"], s)
  save.saveData("hired_list", [], s)
  save.saveData("daysUntilEmployeePayday", 14, s)
  save.saveData("bankrupt", False, s)
  save.saveData("wood", 0, s)
  save.saveData("screws", 0, s)
  save.saveData("pvp_pipes", 0, s)
  
  
  
  print("Your new save will be titled " + new_save_name + ".")
  time.sleep(3)
  
  intro_sequence.intro(s)

#reset saves.json to contain an emty json for testing purposes, if param is true
if 1 == 11:
  saves = open("saves.json", "w")
  saves.write("{}")
  saves.close()

#begin game
print("Home Depot Simulator\n")
aa = input("1. New Game\n2. Load Save\n")
while (aa != ("1") and aa != ("2")):
  print("Invalid")
  aa = input("1. New Game\n2. Load Save\n")
if aa == "1":
  newSave()
  
elif aa == "2":
  #load game
  saves = open("saves.json", "r") #opens saves.json
  saves_dict = json.loads(saves.read()) #sets saves_dict to a python dictionary
  ab = 0
  saves_list = list(saves_dict)
  os.system('clear')
  if len(saves_dict) == 0:
    print("There are no saved games. Press Enter to create a new save.\n")
    input()
    newSave()
  else:
    print("Current saved games:\n")
    #print each save's "name" value
    while ab < len(saves_dict):
      print(str(ab + 1) + ". "+ saves_dict["save" + str(ab)]["name"])
      ab += 1
      
    selected_save = input("Which would you like to load? Or enter n for a new game.\n").lower()
    shouldExit = False
    while shouldExit == False:
      if selected_save == "n":
        shouldExit = True
        newSave()
      elif type(int(selected_save)) == type(1):
        if ("save" + str(int(selected_save) - 1)) in saves_list:
          shouldExit = True
          main_hud.open("save" + str(int(selected_save) - 1))
        else:
          print("Invalid.")