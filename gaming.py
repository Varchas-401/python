v = 7
chance = 0
while chance < 5:
    number  = int(input("Enter your number"))
    print("Let's check ")
    if (v == number):
        print("You are GENIUS!")
        break
    else:
        print("sorry you lose")
        chance += 1


