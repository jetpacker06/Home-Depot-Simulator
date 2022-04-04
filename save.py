import json
def saveData(key, value, save):
  saves = open("saves.json", "r")
  saves_dict = json.loads(saves.read())
  saves.close()
  
  saves_dict[save][key] = value

  saves = open("saves.json", "w")
  saves.write(json.dumps(saves_dict))
  saves.close()