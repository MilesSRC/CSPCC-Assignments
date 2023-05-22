#*****************************************************************************
# Author:           Miles Rush
# Lab:              Assignment 2
# Date:             04/29/2023
# Description:      This program will take in a users weight and height to
#                   give the users BMI (Body Mass Index) number.
#                   It'll also return the persons weight category as defined by 
#                   the WHO (World Health Organization)
# Input:            Weight (lbs), Height (Feet and Inches) 
# Output:           BMI calcuation and BMI category 
# Sources:          Assignment 2 Specifications
#*****************************************************************************
# Neither comments nor code should be wider than 79 characters.
# The lines of asterisks above are 79 characters long for easy reference.
# KGs to Pounds conversion rate
KILOGRAM = 0.45359237

# Feet & Inches to meters conversion rate
METER = 0.0254

# Main function
def main():
    # Introduction
    print("Welcome to the BMI calculator! :) \n" + \
          "This program will calculate your BMI and BMI category for you. \n")

    # Get the users weight in LBs
    weight = ask(float, "What is your weight in pounds/lbs: ")

    # Convert the weight to kilograms for calculation
    weight *= KILOGRAM

    # Get the users height in feet and inches
    heightFeet = ask(int, "What is your height in feet: ")
    heightInches = ask(float, "What is your height in inches: ")

    # Get the users height in meters
    totalInches = (heightFeet * 12) + heightInches
    heightMeters = totalInches * METER

    # Calculate the users bmi using weight / (height ^ 2) = bmi
    bmi = weight / (heightMeters ** 2)

    # Get the users BMI category
    if bmi <= 18.5:
        bmiCategory = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmiCategory = "Normal weight"
    elif bmi >= 25.0 and bmi <= 29.9:
        bmiCategory = "Pre-obesity"
    elif bmi >= 30.0 and bmi <= 34.9:
        bmiCategory = "Obesity class I"
    elif bmi >= 35.0 and bmi <= 39.9:
        bmiCategory = "Obesity class II"
    else:
        bmiCategory = "Obesity class III"

    # Output our results to the user
    print("\nYour BMI: " + format(bmi, '.1f') + "\n"
          "Your BMI Category is \"" + bmiCategory + "\" as defined by WHO.")

# Takes in a function (such as float or int) and asks for input from the
# user. If the user inputs something that causes the program to error, the
# error will be caught and the question will be asked again.
def ask(fn, question):
    try:
        answer = fn(input(question))
        return answer
    except:
        print("Invalid response! Please try again. \n")
        return ask(fn, question)

# Run the main function to start the program
main()