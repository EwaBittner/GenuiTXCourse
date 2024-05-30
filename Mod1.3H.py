# Ex.1 Even or odd

userInput = int(input("Enter a number: "))
if userInput % 2 != 0:
    print("The number is odd.")
else:
    print("The number is even.")


# Ex.2 Temp converter

inputTemp = input("Enter temperature: ")
inputScale = input("Enter C for Celsius or F for Fahrenheit: ")

if inputScale == "C" or inputScale == "c":
    calcF = (int(inputTemp) * 1.8) + 32
    print(f"Entered value {inputTemp}{inputScale} is {calcF}F.")
elif inputScale == "F" or inputScale == "f":
    calcC = (int(inputTemp) - 32) / 1.8
    print(f"Entered value {inputTemp}{inputScale} is {calcC}C.")

# Ex.3 BMI calculator

mass = int(input("Enter your mass in kg: "))
height = float(input("Enter your height in m: "))
bmi = mass / height**2

print("Your BMI is ", round(bmi, 2))
