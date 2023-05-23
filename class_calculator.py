#import tkinter for GUI
import tkinter as tk
#Make a class calculator with the functions
class Calculator:

#Create window for calculator

    #Window format
    def window(self):
        self.root = tk.Tk()
        self.root.title("Simple App Calculator")
        #Get two numbers from the user

        self.number_1_label = tk.Label(self.root, text="Please enter first number: ")
        self.number_2_label = tk.Label(self.root, text="Please enter second number: ")
        #Choose operation

        #Button for user input

        #Button for operation

        #Button for calculation

        #Message box for the result or error message

        self.root.mainloop()

#Function for calculation
    #Try and except to ask the user again if they enter a string or character

    




  


