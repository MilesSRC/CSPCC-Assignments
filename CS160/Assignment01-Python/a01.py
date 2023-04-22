#*****************************************************************************
# Author:       	Miles Rush
# Lab:          	Assignment 1
# Date:         	04/22/2023
# Description:  	Calculates the time to travel a certain distance
# Input:        	Inputs for:
#                   - Distance to travel (In Miles)(Integer)
#                   - Traveling speed (In Miles Per Hour)(Integer)
# Output:       	"You will arrive at your destination in X minutes"
# Sources:      	N/A
#*****************************************************************************
# Neither comments nor code should be wider than 79 characters.
# The lines of asterisks above are 79 characters long for easy reference.
HOUR = 60;

def main():
    # Introduction
    print("Welcome! This program will calculate the time needed " + \
          "to travel a set distance.")
    print("");

    # Get the distance and speed values from the user
    distance = int(input("How far is the destination? (In Miles): "));
    speed = int(input("What is your traveling speed? (In MPH): "));

    # Calculate the distance over speed formula to get the hours (in fraction)
    # it will take to travel that distance. Then, times the value by an hour
    # for the time in minutes.
    time = (distance / speed) * HOUR;

    # Change time to a string and format it to two decimal poitns for output
    timeString = str(format(time, '.2f'));

    print("")
    print("You will arrive at your destination in " + timeString + " minutes.")

main();