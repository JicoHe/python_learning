# function with multiple parameter
def describe_pet(animal_type, pet_name='Willie'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'wangwang')
describe_pet(animal_type='dog')
