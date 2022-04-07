import datetime
def log(input):
  log = open(".log", "a")
  log.write(str(datetime.datetime.now()) + " ")
  log.write(str(input))
  log.write("\n")
  #To write to the log:
  """
  logger.log(anything)
  """