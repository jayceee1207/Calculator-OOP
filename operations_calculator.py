#create class operations
class operations():
    
    #Addition Function
    def add(self, number1, number2):
        return number1 + number2
    #Subtraction Function
    def subtract(self, number1, number2):
        return number1 - number2

    #Multiplication Function
    def multiply(self, number1, number2):
        return number1 * number2
    
    #Division Function
    def divide(self, number1, number2):
        #If the the divisor is equal to 0, it will raise an error message
        if number2 == 0:
            raise ZeroDivisionError("Second number must not be 0")
        
        #Else, it will return the quotient
        else:
            return number1 / number2


