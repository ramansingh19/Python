# name = "Raman"

# def func():
#   name = "Aman"
#   print(name)

# func()
# print(name)

# x = 99

# def func2(y):
#   n = x + y
#   return n

# result = func2(1)
# print(result)

# x = 69

# def f1():
#   x = 90
#   def f2():
#     print(x)
#   f2()
# f1()


def c1(x):
  def c2(y):
    return x ** y
  return c2

f = c1(2)
g = c1(3)


print(f(3))
print(g(3))



