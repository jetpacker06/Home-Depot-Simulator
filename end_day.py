import save
import minigame
import random
import pay_employees
import math

def end_day(s):
  #calculate earnings for day
  save.saveData("daysUntilEmployeePayday", save.getData("daysUntilEmployeePayday", s) - 1, s)
  
  if save.getData("daysUntilEmployeePayday", s) == 0:
    pay_employees.pay(s)

def dayOverview(s):
 
  if len(save.getData("hired_list", s)) != 0:
    
    hiredArr = save.getData("hired_list", s)
    if type(hiredArr) == type(None):
      hiredArr = []
    employeeCount = len(hiredArr)
    employeeMulti = 1
    i = 0
    #for each employee, the total amount of each item sold multiplies by 1.2
    while i < employeeCount:
      employeeMulti *= 1.2
      i += 1
    woodmulti = math.ceil(random.randint(1, 30)) / 100
    screwmulti = math.ceil(random.randint(1, 30)) / 100
    pipemulti = math.ceil(random.randint(1, 30)) / 100
  
    woodSold = math.ceil(math.ceil(woodmulti * save.getData("wood", s)) * employeeMulti)
    screwsSold = math.ceil(math.ceil(screwmulti * save.getData("screws", s)) * employeeMulti)
    pipesSold = math.ceil(math.ceil(pipemulti * save.getData("pvc_pipes", s)) * employeeMulti)
  
    total = (woodSold * 5) + (screwsSold * 2) + (pipesSold * 3)
    totalSold = woodSold + screwsSold + pipesSold
    
    total = math.ceil(total)
    totalSold = math.ceil(totalSold)
    print("Your workers sold ", totalSold, "items, and you made $", total)
    print("Wood sold:" + str(woodSold))
    print("Profit:" + str(woodSold * 5))
    print("Screws sold:" + str(screwsSold))
    print("Profit:" + str(screwsSold * 2))
    print("PVC Pipes sold:" + str(pipesSold))
    print("Profit:" + str(pipesSold * 3))
    input("\nPress enter to continue.")
    #save balance
    save.saveData("balance", save.getData("balance", s) + total, s)
    #save amounts of stock remaining
    save.saveData("wood", (save.getData("wood", s) - woodSold), s)
    save.saveData("screws", (save.getData("screws", s) - screwsSold), s)
    save.saveData("pvc_pipes", (save.getData("pvc_pipes", s) - pipesSold), s)
    
  else:
    print("You didn't hire any employees! Nothing got done today...")
    input("\nPress enter to continue.")