#Class & Object
class Car:
  def __init__(self ,__userbrand , usermodel):
    self.__userbrand = __userbrand
    self.__usermodel = usermodel

  #Encapsulation --> when we want privatisation we use __ this symbol so we when we want to access brand we have to call get_brand first ,
  def get_brand(self):
    return self.__userbrand + "!"

  def fullname(self):
    return f"{self.__userbrand} , {self.__usermodel}"

  def fuel_type(self):
    return "Desiel or Petrol"
  
  @staticmethod
  def description():
    return "This car is One the Fastest car you ever see!"
  
  @property
  def model(self):
    return self.__usermodel

#inheritance
class ElectricCar(Car):
  def __init__(self , __userbrand , usermodel , battery_size):
    super().__init__(__userbrand , usermodel)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric"

my_electricCar = ElectricCar("Tesla" , "S" , "500kwh")

c = Car("BMW", "M4")
c.usermodel = "lexus"


my_TeslaCar = ElectricCar("Tesla" , "S" , "500kwh")
print(isinstance(my_TeslaCar , Car))
print(isinstance(my_TeslaCar , ElectricCar))


# print(c.model)

# print(c.description())
# print(Car.description())

# print(c.fuel_type())
# print(my_electricCar.fuel_type())

# print(my_electricCar.userbrand)
# print(my_electricCar.fullname())
# print(my_electricCar.__userbrand)
# print(my_electricCar.get_brand())

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


