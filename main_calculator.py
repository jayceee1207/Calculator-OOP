#import Calculator
from class_calculator import Calculator
#Call function from Calculator class


calc = Calculator()

#print title
calc.title()

#print message for the user
calc.message()


while True:
    #input numbers
    calc.input_numbers()

    #choose operation
    calc.operation()

    #perform calculation
    calc.calculations()

    #display result
    calc.result()
