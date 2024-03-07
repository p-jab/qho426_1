name = input("Enter your name: ")

if len(name) > 5:
    print("You have a long name!")
elif len(name) < 3:
    print("Your name is soooooooo short!")
elif name.lower() == "piotr":
    print("That's the best name")
else:
    print("That's not a name. I call you bob")
print("Welcome to Python classes")