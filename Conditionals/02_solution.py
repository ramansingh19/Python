age = int(input('Tell me your age: '))
day = 'wednesday'

if(age < 18):
  price = 8
else:
  price = 12

if day == 'wednesday':
  price = price - 2

print(f"Ticket price is ${price}") 

#another method 
# age = int(input("Tell me your age: "))
# day = "wednesday"

# price = 8 if age < 18 else 12

# if day == "wednesday":
#     price -= 2

# print(f"Ticket price is ${price}")