# 使用继承
from car import Car

# 定义电池的类
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self, range=260):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    """初始化父母类的属性"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 创建了Battery的实例
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")


# 在创建子类的实例，实例先调用子类的__init__()方法，在呼唤父类的__init()__方法
my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery = Battery(75)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()