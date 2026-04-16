class Battery:
  def battery_info(self):
    return "Hello from battery"

class Engine:
  def engine_info(self):
    return "Hello from Engine"

class ElectricCar(Battery , Engine):
  pass


c = ElectricCar()
print(c.battery_info())
print(c.engine_info())