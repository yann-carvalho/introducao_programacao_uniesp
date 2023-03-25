age = int(input("State your age: "))

if age > 17:
    print("You can enter the party")
elif age > 16 and age < 18:
    print("Go back home")
else:
    print("You can't enter the party")