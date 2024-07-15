from car import ElectricCar

my_SU = ElectricCar('Xiaomi', 'su7', 2023)
print(my_SU.get_descriptive_name())
my_SU.battery.describe_battery()
my_SU.battery.get_range()