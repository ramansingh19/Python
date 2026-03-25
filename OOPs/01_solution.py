class Car():
  def __init__(self ,userbrand , usermodel):
    self.userbrand = userbrand
    self.usermodel = usermodel


my_car = Car("BMW" , "M4")
print(my_car.userbrand)
print(my_car.usermodel)


# self is use for communication btw these objects just like this in JS.


# instead of self we can use anything , in this example i use this 
# class Car():
#   def __init__(this ,userbrand , usermodel):
#     this.userbrand = userbrand
#     this.usermodel = usermodel


# my_car = Car("BMW" , "M4")
# print(my_car.userbrand)
# print(my_car.usermodel)