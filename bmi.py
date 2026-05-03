'''
Henry Petzinger
IS303 - A01

BMI Calculator
This program calculates body mass index from height and weight

Inputs:
-name (string)
-height in inches(float)
-weight in pounds(float)

Processes:
-Convert height and weight to floats
-BMI = (weight / height ** 2) * 703

Outputs:
-Print the BMI number next to the inputs of name height and weight for clarity

'''
name = input("What is your name?")
weight = float(input("What is your weight in pounds?"))
height = float(input("What is your height in inches?"))

BMI = (weight / height ** 2) * 703

print(f"{name} | {height} inches | {weight} pounds | BMI: {BMI:.2f}")



