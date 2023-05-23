#import tkinter for GUI
import tkinter as tk
#Make a class calculator with the functions
class Calculator:

#Create window for calculator
    def __init__(self, calculator):
        self.calculator = calculator
        self.window

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

        self.operation_var = tk.StringVar(value = "Choose operation")

        #make a menu where the user will choose any operation from list
        #Button for user input

        #Button for operation

        #Button for calculation

        #Message box for the result or error message

        self.root.mainloop()

#Function for calculation
    #Try and except to ask the user again if they enter a string or character

    




  


