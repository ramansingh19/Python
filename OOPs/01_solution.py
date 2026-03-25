#Class & Object
class Car:
  def __init__(self ,userbrand , usermodel):
    self.userbrand = userbrand
    self.usermodel = usermodel

  #Encapsulation --> when we want privatisation we use __ this symbol so we when we want to access brand we have to call get_brand first ,
  def get_brand(self):
    return self.__userbrand + "!"

  def fullname(self):
    return f"{self.userbrand} , {self.usermodel}"

#inheritance
class ElectricCar(Car):
  def __init__(self , battery_size , userbrand , usermodel):
    super().__init__(userbrand , usermodel)
    self.battery_size = battery_size

my_electricCar = ElectricCar("Tesla" , "S" , "500")

# print(my_electricCar.userbrand)
print(my_electricCar.get_brand())
# print(my_electricCar.fullname())

# my_car = Car("BMW" , "M4")
# print(my_car.userbrand)
# print(my_car.usermodel)
# print(my_car.fullname())




# self is use for communication btw these objects just like this in JS.


# instead of self we can use anything , in this example i use this 
# class Car():
#   def __init__(this ,userbrand , usermodel):
#     this.userbrand = userbrand
#     this.usermodel = usermodel


# my_car = Car("BMW" , "M4")
# print(my_car.userbrand)
# print(my_car.usermodel)


