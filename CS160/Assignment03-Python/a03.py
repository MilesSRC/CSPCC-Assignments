#*****************************************************************************
# Author:           Miles Rush
# Lab:              Assignment 3
# Date:             05/14/2023
# Description:      
#                   
# Input:            
# Output:           
# Sources:          Assignment 3 Specifications
#*****************************************************************************
# Neither comments nor code should be wider than 79 characters.
# The lines of asterisks above are 79 characters long for easy reference.

def main():
    # Welcome message
    print("Welcome to the book inventory program! \n" + \
          "You'll put in your current inventory of books and get helpful\n" + \
          "information about your inventory at the end. \n")

    # Define our parallel lists
    # These will store our book titles and associated quantities
    book_titles = []
    book_quantities = []

    # Let's ask for the book titles and quantities
    while input("Would you like to add a book? (y/n) ").lower() == "y":
        # New line to make the UI prettier
        print()

        # Ask for some meta data about the book
        book_name = ask(str, "What is the title of this book? ")
        book_quantity = ask(int, "How many units of this book are in stock? ")

        # Now, we'll append these so that they are parallel
        book_titles.append(book_name)
        book_quantities.append(book_quantity)

        # New line to make the UI prettier
        print()

    # New line for organization
    print()

    # Let's then summarize the linked lists and
    # find the highest and lowest book in stock
    # and get the index so we can retrieve the names of the books
    highest_index = book_quantities.index(max(book_quantities))
    lowest_index = book_quantities.index(min(book_quantities))

    # Print the book with the most copies in stock
    print(book_titles[highest_index], "is the book with the most copies.")

    # Print the book with the least copies
    print(book_titles[lowest_index], "is the book with the least copies.")

    # Thank you
    print("\nThank you for using the Book Inventory Program. :)")

# Takes in a function (such as float or int) and asks for input from the
# user. If the user inputs something that causes the program to error, the
# error will be caught and the question will be asked again.
def ask(fn, question):
    try:
        answer = fn(input(question))
        return answer
    except:
        print("Invalid response! Please try again.")
        return ask(fn, question)

# Run the program
main()