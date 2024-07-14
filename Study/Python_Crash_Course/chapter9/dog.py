# 使用类定义一只狗
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!.")

# 创建实例
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()