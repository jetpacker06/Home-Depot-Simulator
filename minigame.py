import random
import save
import logger
def play(s):
  gameList = ["op1", "op2"]
  choice = random.choice(gameList)
  print(choice)
  logger.log(choice)