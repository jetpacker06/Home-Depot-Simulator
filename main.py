import json
import intro_sequence
import time
import save
import get_saves_count
"""
The player now has the ability to create a new save of their desired title.
This creates a new key in saves.json, with its value being a nested
dictionary. this nested dictionary starts with just "name":(their entered save name)
but we will use this nested dictionary to save other things as well.
"""


#backup saves.json
if 1 == 11:
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
  #new save
  #request new name, create new save, create name of new save, move on to intro
  
  new_save_name = input("Enter the name of your new save.\n")
  saves = open("saves.json", "r")
  saves_dict = json.loads(saves.read())
  saves.close()
  saves_dict["save" + str(get_saves_count.getSavesCount())] = {"name":new_save_name}
  saves = open("saves.json", "w")
  saves.write(json.dumps(saves_dict))
  saves.close()
  print("Your new save will be titled " + new_save_name + ".")
  save.saveData("testkey", "testvalue", "save0")
  time.sleep(3)
  intro_sequence.intro()
  print()
  
elif aa == "2":
  #load game
  saves = open("saves.json", "r") #opens saves.json
  saves_dict = json.loads(saves.read()) #sets saves_dict to a python dictionary
  ab = 0
  saves_list = list(saves_dict)
  print("Current saved games:\n")
  #print each save's "name" value
  while ab < len(saves_dict):
    print(saves_dict["save" + str(ab)]["name"])
    ab += 1