#import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
from operations_calculator import operations


#Class for User interface
class UserInterface(Frame):
    def __init__(self, master):
        #Create widgets
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()
        self.calculator = operations()
        
    def create_widget(self):

        #widget for 1 label
        
        self.title_label = Label(self, text = "SIMPLE CALCULATOR", fg="pink", 
                                 highlightbackground="blue", highlightcolor="red", highlightthickness=2,
                                 font=('Comic Sans MS', 20, "bold"))
        self.title_label.grid(row = 0, column = 1, columnspan = 3)

        self.input1_label = Label(self, text = "Input number 1",  bg="green", fg="white", font=('Courier New', 13, "bold"))
        self.input1_label.grid(row=1, column=0)

        #widget for 1 entry
        self.input1 = Entry(self,width=50, 
                            highlightbackground="black", 
                            highlightcolor="red",
                            highlightthickness=2)
        self.input1.grid(row=1, column=1)
        
        #widget for 2 label
        self.input2_label = Label(self, text = "Input number 2", bg="green", fg="white", font=('Courier New', 13, "bold"))
        self.input2_label.grid(row=2, column=0)

        #widget for 2 entry
        self.input2 = Entry(self,width=50, 
                            highlightbackground="black", 
                            highlightcolor="red",
                            highlightthickness=2)
        self.input2.grid(row=2, column=1)   

        #widget for operator
        self.operator_label = Label(self, text = "Choose operator:", fg = "blue", font=('Courier New', 12, "bold"))
        self.operator_label.grid(row=3, column=1)   

        #initial value is operator
        self.operator_var = StringVar(self)
        self.operator_var.set("Addition")

        #create a menu functions
        self.operator_options = OptionMenu(self, self.operator_var, "Addition", "Subtraction", 
                                           "Multiplication", "Division", "Remainder")
        self.operator_options.grid(row=4, column=1)

    
        #calculations
        self.button = Button(self, text = "Result!", relief=tk.RAISED, 
                             bg="blue", fg="white", width=20, borderwidth= 3, command=self.press_button)
        self.button.grid(row=5, column=1)
        
        #display result
        self.result_label = Label(self, text ="")
        self.result_label.grid(row=5, column=1)

    #We have to make press button method for buttons
    def press_button(self):
        #try and except for values
        try:
            #get the values
            number1 = self.input1.get()
            number2 = self.input2.get()
            operator = self.operator_var.get()

            #perform calculations
            #addition
            if operator == "Addition":
                result = self.calculator.add(int(number1), int(number2))
            #subtraction
            elif operator == "Subtraction":
                result = self.calculator.subtract(int(number1), int(number2))
            #multiplication
            elif operator == "Multiplication":
                result = self.calculator.multiply(int(number1), int(number2))
            #division
            elif operator == "Division":
                result = self.calculator.divide(int(number1), int(number2))

            #remainder
            elif operator == "Remainder":
                result = self.calculator.remainder(int(number1), int(number2))

            self.result_label.config(text= result)

        #Add error handling
        except ValueError:
            self.result_label.config(text="Invalid input. Try again!", bg="red")

        #remove inputs
        self.input1.delete(0, END)
        self.input2.delete(0, END)
