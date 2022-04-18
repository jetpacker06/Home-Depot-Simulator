import random
import save
RobsImpulse = [0, 1]
def robbery():
  #When day changes :
  random.choices(RobsImpulse, weights=(95, 5))
  if RobsImpulse == 1:
    print("Rob the Notorious Robber robbed your store!!")
    (save.getData("balance", ))
    #idk how to change the balance ;_;
    #There is am 8% chance of a pedophile walking in and harassing the customer(the chance is low because       he is in jail most days, but his paroll officer is lazy)
  #why^