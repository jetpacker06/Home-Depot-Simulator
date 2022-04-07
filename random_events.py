import random
import save
RobsImpulse = [0, 1]
def robbery():
  #When day changes :
  random.choices(RobsImpulse, weights=(95, 5))
  if RobsImpulse == 1:
    print("Rob the Notorious Robber robbed your store!!")
    (save.getData("balance", s))