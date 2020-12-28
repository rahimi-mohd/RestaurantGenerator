import random, time

print("Welcome to Restaurant Generator")
restaurant = input("Please insert restaurant name: \n").split()
print("Processing...")
time.sleep(2)

def WhereToEat(restaurant):
    return random.choice(restaurant)

print(f"We will eat at {WhereToEat(restaurant)} !")
time.sleep(2)
print("Enjoy your meal.")
quit = input('Press enter to quit()')
