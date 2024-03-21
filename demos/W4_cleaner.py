def dimensions():
    w = float(input("Enter the width of the room: "))
    l = float(input("Enter the length of the room: "))
    return w*l

#total = dimensions() + dimensions() + dimensions()
#print(total)

def r_name():
    return input("Enter room type: ")

# room1 = r_name()
# room2 = r_name()
# print(f"We have {room1} and {room2}")

def price(name="", area=1):
    if name.lower() == "bathroom":
        return 15*area
    elif name.lower() == "bedroom":
        return 10*area
    else:
        return 5*area

# print(price("bathroom", 20))
# print(price("bedroom", 10))

def run():
    t_price = 0
    num = int(input("Enter number of rooms to be cleaned: "))
    for i in range(num):
        room = r_name()
        area = dimensions()
        p = price(room, area)
        t_price += p
    print(f"The total price is £{t_price}")

run()
