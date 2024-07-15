# 9-1 使用方法
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")
        print(f"The number served is {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


# 9-2
restaurant_A = Restaurant('KFC', 'fast food')
restaurant_B = Restaurant('BMW', 'milk')
restaurant_C = Restaurant('McDonald', 'fast food')
restaurant_A.describe_restaurant()
restaurant_B.describe_restaurant()
restaurant_C.describe_restaurant()


# 9-3
class User:
    def __init__(self, first_name, last_name, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} {self.gender} {self.login_attempts}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# 9-4
restaurant = Restaurant('塔斯汀', '中国汉堡')
restaurant.describe_restaurant()

restaurant.set_number_served(5)
restaurant.describe_restaurant()

restaurant.increment_number_served(1)
restaurant.describe_restaurant()

# 9-5
user = User('Jico', 'He', 'male', 0)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
user.reset_login_attempts()
user.describe_user()


# 9-6 冰淇淋小铺
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Strawberry', 'Watermelon', 'Milk']

    def describe_flavor(self):
        print("We have these flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


IceCreamStand = IceCreamStand('Mcdonald', 'Sweet')
IceCreamStand.describe_flavor()

# 9-7 9-8 用户中的管理员
class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print(f"You have these privileges:\n{self.privileges}")

class Admin(User):
    def __init__(self, first_name, last_name, gender, login_attempts):
        super().__init__(first_name, last_name, gender, login_attempts)
        self.privileges = Privileges()


Admin = Admin('Jico', 'He', 'male', '0')
Admin.privileges.show_privileges()

# 9-9 见源文件