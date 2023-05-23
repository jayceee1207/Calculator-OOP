#create class operations
class operations():
    
    #Addition Function
    def addition(self, number1, number2):
        return(self + str(number1 + number2))
    #Subtraction Function
    def subtraction(self, number1, number2):
        return(self + str(number1 - number2))

    #Multiplication Function
    def multiplication(self, number1, number2):
        return(self + str(number1 * number2))
    
    #Division Function
    def division(self, number1, number2):
        #The quotient will be displayed if number 2 is not equal to zero
        if number2 :
            return(self + str(number1 / number2))
        
        #Else, it will raise an error
        else:
            raise ZeroDivisionError("Second number must not be 0")


