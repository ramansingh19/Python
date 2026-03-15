n = int(input("Give me one number"))
even_count = 0

for i in range(1, n+1):
  if i%2 == 0:
    even_count += 1
print(even_count)