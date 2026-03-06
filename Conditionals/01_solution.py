age = int(input('Give me your age : '))
# age = 12
if age <= 13:
  print('Child')
elif 13 < age <= 19:
  print('Teenager')
elif 20 < age <= 59:
  print('Adult')
elif age >= 60:
  print('Senior')