#create class operations
class operations():
    
    #Addition Function
    def add(self, number1, number2):
        return("Sum: " + (number1 + number2))
    #Subtraction Function
    def subtract(self, number1, number2):
        return("Difference: " + str(number1 - number2))

    #Multiplication Function
    def multiply(self, number1, number2):
        return("Product: " + str(number1 * number2))
    
    #Division Function
    def divide(self, number1, number2):
        #The quotient will be displayed if number 2 is not equal to zero
        if number2 :
            return("Quotient: " + str(number1 / number2))
        
        #Else, it will raise an error
        else:
            raise ZeroDivisionError("Second number must not be 0")


