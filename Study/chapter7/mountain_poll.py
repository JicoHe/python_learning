responses = {}
# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday")
    # store the response in the dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond?(y / n)")
    if repeat == "n":
        polling_active = False

print("\n---- Poll Results ----")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")

