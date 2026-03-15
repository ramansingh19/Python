import time

wait_time = 1

for retry in range(3):
  print("attempt" , retry + 1)

  success = False

  if success:
    print("success")
    break
  else:
    print("Failed. Retrying in", wait_time, time.sleep(wait_time))

    wait_time *= 2