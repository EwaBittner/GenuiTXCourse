print("Hi, my name is Age calculator!")
name = input("What is your name? ")

if name[0] == "A":
    name = input("Please provide your name once more: ")

surname = input("What is your last name? ")

if surname[-1] == "a":
    surname = "Doe"
age = input("How old are you? ")

totalAge = int(age) + 50

if totalAge >= 100:
    result = "Old"
elif totalAge > 30:
    result = "Young"

print(f"User {name} {surname} will be {totalAge} in 50 years.")
print(result)
