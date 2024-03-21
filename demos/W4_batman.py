from random import randint

def batman_punch(str = 5, technique = 5):
    punch_power = 0.4 * str + 0.6 * technique
    return punch_power

# print(f"Batman punch with {batman_punch(8, 10)} power")
# print(f"Batman punch with {batman_punch(4)} power")
# print(f"Batman punch with {batman_punch(technique = 10)} power")

def fight_scene(n=2, enemy_str = 3):
    total_str = n*enemy_str
    bat_str = batman_punch(randint(0,10), randint(0,10))
    if bat_str >= total_str:
        return "Batman wins!"
    else:
        return "Batman is beaten!"

def roberry_escape(n_cars):
    if n_cars > 5:
        return "Batman is caught"
    else:
        return "Batman escapes"

def run():
    scene = fight_scene(randint(1,5), randint(1,5))
    escape = roberry_escape(randint(1,8))
    print(f"After a long fight, {scene}. Afterwards, police chase him and {escape}")

run()