#Because it take reference that why it is show aman 

# name = "Raman"
# name[1] = "A" #you can not change its value if once decalre it .

# name = "Mman"
# print(name)

#another example 
x = 10 
y = x
# print(x)
# print(y)
x = 30;
# print(x)
# print(y) #Becauese it is reference does not change that why .



# #mutuable --> we change the value without creating new Object
num = [1,2,3,4]
num[2] = 10;
# print(num)

#another 
nums = [1, 2, 3]
# print(id(nums))

nums.append(4)
# print(id(nums))


# -----------------Interview pov------------
#both are changing in same 
a = {1, 2, 3}
b = a
b.add(4)

# print(a)
# print(b)

a = [1, 2, 3]
b = a
b.append(4)

# print(a)
# print(b)


def add_item(item , my_list=[]):
  my_list.append(item)
  return my_list;

print(add_item(1))
print(add_item(2))
print(add_item(3))

