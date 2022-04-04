import json
def getSavesCount():
  saves = open("saves.json", "r")
  saves_dict = json.loads(saves.read())
  saves_list = list(saves_dict)
  saves.close()
  return len(saves_dict.keys())