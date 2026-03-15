n = 22
prime = True

if n > 1:
  for i in range(2, n):
    if (n % i) == 0:
      prime = False
      break

print(prime)