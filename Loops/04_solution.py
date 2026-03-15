# reverse string

name = "test"
reverse_name = ""

for char in name:
  reverse_name = char + reverse_name

print(reverse_name)


num = 988
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)