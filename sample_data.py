
print("Welcome to the BMI Calculator!")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

if weight <= 0 or height <= 0:
    print("Error: Weight and height must be greater than zero.")
else:
    bmi = weight / (height ** 2)

    print("Your weight:", weight, "kg")
    print("Your height:", height, "m")
    print("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
