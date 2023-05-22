#Make a class calculator with the functions
class Calculator:
    #Title function
    def title(self):
        print("Calculator")
    #Message function
    def message(self):
        print("Please enter two numbers and operation")

    #Input two numbers
    def input_numbers(self):
        #While True. If the user input a string or character. It will give an error message
        while True:
            try:
                self.num1 = float(input("Please enter number 1: "))
                self.num2 = float(input("Please enter number 2: "))
                break
            except:
                print("Invalid input. Try again!")
                continue

    #Perform operation
    def operation(self):
        while True:
            try: 
                print("Please choose an option from the menu.")
                print("[1] Operation 1:","Addition")
                print("[2] Operation 2:","Subtraction")
                print("[3] Operation 3:","Multiplication")
                print("[4] Operation 4:","Division")
                self.option = int(input("Enter operation: "))
                break
                
            except:
                print("Invalid input. Try again!")
                continue
    def calculations(self):
        if self.option == 1:
            self.add_num = self.num1 + self.num2
           


    #Display Result
    def result(self):
        print(self.add_num)

    #Thank you message