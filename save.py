import json
def saveData(key, value, s):
  saves = open("saves.json", "r")
  saves_dict = json.loads(saves.read())
  saves.close()
  saves_dict[s][key] = value
  saves = open("saves.json", "w")
  saves.write(json.dumps(saves_dict))
  saves.close()

def getData(key, s):
  saves = open("saves.json", "r")
  saves_dict = json.loads(saves.read())
  saves.close()
  return saves_dict[s][key]