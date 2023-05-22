#import Calculator
from class_calculator import Calculator
#Call function from Calculator class




calc = Calculator()

#print title
calc.title()

#print message for the user
calc.message()


moredata = "Yes"
while moredata == "Yes" or "yes" or "YES" or "y" or "Y":
    #input numbers
    calc.input_numbers()

    #choose operation
    calc.operation()

    #perform calculation
    calc.calculations()

    #display result
    calc.result()

    moredata = (input("Do you want to use the program again? \n[Yes] if continue \n[No] if exit \nEnter option: "))

print("Thank you for using our program!")