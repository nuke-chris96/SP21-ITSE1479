# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2021";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Arcement - call to function goes here
    jumpTable['3'] = stub                 # Burns - call to function goes here
    jumpTable['4'] = stub                 # De Guzman - call to function goes here
    jumpTable['5'] = stub                 # Ezell - call to function goes here
    jumpTable['6'] = stub                 # Goltl - call to function goes here
    jumpTable['7'] = stub                 # Hammad - call to function goes here
    jumpTable['8'] = stub                 # Hopper - call to function goes here
    jumpTable['9'] = stub                 # Newman - call to function goes here
    jumpTable['10'] = stub                # Nguyen - call to function goes here
    jumpTable['11'] = stub                # Rodriguez Rosales - call to function goes here
    jumpTable['12'] = stub                # Seaman - call to function goes here
    jumpTable['13'] = stub                # Silva - call to function goes here
    jumpTable['14'] = stub                # Simmons - call to function goes here
    jumpTable['15'] = smithCFunction      # Smith, C - call to function goes here
    jumpTable['16'] = stub                # Smith, J - call to function goes here
    jumpTable['17'] = stub                # Stout - call to function goes here
    jumpTable['18'] = stub                # Syed - call to function goes here
    jumpTable['19'] = stub                # Watts - call to function goes here
    jumpTable['20'] = stub                # Woolard - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Arcement")
    print("3.  Burns")
    print("4.  De Guzman")
    print("5.  Ezell")
    print("6.  Goltl")
    print("7.  Hammad")
    print("8.  Hopper")
    print("9.  Newman")
    print("10. Nguyen")
    print("11. Rodriguez Rosales")
    print("12. Seaman")
    print("13. Silva")
    print("14. Simmons")
    print("15. Smith, C")
    print("16. Smith, J")
    print("17. Stout")
    print("18. Syed")
    print("19. Watts")
    print("20. Woolard")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************
def smithCFunction():
    print()
    print()
    
    print("Random password generator.\n")
    while True:
        print("Enter length of password: \n")
        try:
            length = int(input(">>> "))
            break
        except ValueError:
            print("\n***Please only enter numerical values***\n")
    
    passwordGen(length)
    input("Press ENTER to continue >>> ")
    
def passwordGen(length):
    import random
    
    password = ''
    
    for i in range(int(length)):
        letter = chr(random.randint(60, 126))
        password += letter
            
    print("\nYour", int(length), "digit password: ", password)       
    print()
    print()
    
# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
