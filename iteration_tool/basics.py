# import time

# print("Raman")

# time.sleep()

# username = "Amam"

# a = [1,2,3]
# b = ['a','b','c']
# print(list(zip(a,b)))

names = ["Ram", "Shyam", "Aman"]
for i, name in enumerate(names):
    print(i, name)


nums = [1,2,3,4]
result = list(map(lambda x: x*2, nums))
print(result)

# set = [1,2,4,4]

# I= iter(set)
# R = (I.__next__())
# print(R)