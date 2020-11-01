import random
import time
startTime = time.time()
while True:
    random.seed()
    loop = random.randint(1, 99999)
    result = random.randoint(1, 99999)
    time.sleep(0.01)
    executionTime = (time.time() - startTime)
    print(loop)
    if loop == result:
      print("Execution time in seconds: " + str(executionTime))
      break
