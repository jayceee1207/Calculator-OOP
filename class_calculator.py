#import tkinter for GUI
import tkinter as tk
from operations_calculator import operations
from tryagain_calculator import TryAgain
#Make a class calculator with the functions
class Calculator:
#Create window for calculator
    def __init__(self, calculator):
        self.calculator = calculator
        self.window()

    #Window format
    def window(self):
        self.root = tk.Tk()
        self.root.title("Simple App Calculator")
        #Get two numbers from the user

        self.number1_label = tk.Label(self.root, text="Please enter first number: ")
        self.number2_label = tk.Label(self.root, text="Please enter second number: ")

        self.number1_entry = tk.Entry(self.root)
        self.number2_entry = tk.Entry(self.root)

        #Grid and label for number 1 and 2. sticky means we will put the label on the east side or right side
        self.number1_label.grid(row=0, column=0, sticky="e")
        self.number2_label.grid(row=1, column=0, sticky="e")

        self.number1_entry.grid(row=0, column=1)
        self.number2_entry.grid(row=1, column=1)
        #Choose operation
        
        self.operation = tk.StringVar(value = "Choose operation")
        #make a menu where the user will choose any operation from list
        self.operation_menu = tk.OptionMenu(self.root, self.operation, "Addition","Subtraction","Multiplication","Division")
        self.operation_menu.grid(row=2, column=0, columnspan=2, pady=5)

        #Button for calculation
        self.calculate_button = tk.Button(self.root, text="Click",command = self.calculation)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=5)
        
        #Message box for the result or error message
        self.result_label = tk.Label(self.root, text="RESULT:")
        self.result_label.grid(row=4, column=0, columnspan=2)

        #ask if they want to try again
        self.ask_again = TryAgain(self.root, self.result_label, self.number1_entry, self.number2_entry)

        self.root.mainloop()

    #Function for calculation
    def calculation(self):
        #Try and except to ask the user again if they enter a string or character
        try:
            number1 = float(self.number1_entry.get())
            number2 = float(self.number2_entry.get())
            operation = self.operation.get()
        
            if operation == "Addition":
                result = self.calculator.add(number1, number2)
            elif operation == "Subtraction":
                result = self.calculator.subtract(number1, number2)
            elif operation == "Multiplication":
                result = self.calculator.multiply(number1, number2)
            elif operation == "Division":
                result = self.calculator.divide(number1, number2)
        
            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid input. Try again!")
        except ZeroDivisionError as e:
            self.result_label.config(text=str(e))

        self.ask_again.ask()
        




  


