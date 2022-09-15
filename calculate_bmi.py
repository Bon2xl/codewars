# Calculate BMI
# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

def bmi(weight, height):
    #your code here
    bmi = round(weight / (height * height), 2)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"

print(bmi(50, 1.80))
