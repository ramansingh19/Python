distance = int(input('Tell me distance: '))

if distance < 3:
  print('Walk')
if 3 < distance <= 15:
  print('Bike')
if distance > 15:
  print('Car')
