import random

responses = ["yes", "no", "maybe"]

while True:
    q = input("What would you like to know? (or q to quit)\n    ")

    if q == "q":
        break

    print("    " + random.choice(responses))
