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
  saves_dict[s] = {"name":new_save_name}
  saves = open("saves.json", "w")
  saves.write(json.dumps(saves_dict))
  saves.close()
  print("Your new save will be titled " + new_save_name + ".")
  time.sleep(3)
  save.saveData("balance", 1000, s)
  save.saveData("unhired_list", ["Jeff", "Mark", "Barbara", "Jimothy", "Margaret", "Vanessa", "Roland", "Clarence", "Loretta"], s)
  save.saveData("hired_list", [], s)
  save.saveData("daysUntilEmployeePayday", 14, s)
  intro_sequence.intro(s)

#reset saves.json to contain just a single save if the param is true, just for testing purposes
if 1 == 1:
  saves = open("saves.json", "w")
  savesBackup = open("savesBackup.txt", "r")
  saves.write(savesBackup.read())
  saves.close()
  savesBackup.close()

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
  print("Current saved games:\n")
  #print each save's "name" value
  while ab < len(saves_dict):
    print(str(ab + 1) + ". "+ saves_dict["save" + str(ab)]["name"])
    ab += 1
  selected_save = input("Which would you like to load? Or enter n for a new game.\n".lower())
  
  if selected_save == "n":
    newSave()
  elif type(int(selected_save)) == type(1):
    if ("save" + str(int(selected_save) - 1)) in saves_list:
      print("yes it was")
      main_hud.open("save" + str(int(selected_save) - 1))
    else:
      print("nope")