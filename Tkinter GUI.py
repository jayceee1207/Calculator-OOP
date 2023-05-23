#import tkinter
from tkinter import *
from operations_calculator import operations
#Class for User interface
class UserInterface(Frame):
    #Init frame
    def __init__(self, master):
        #Create widgets
        Frame.__init__(self,master)
        self.grid
        self.create_widget()
        self.calculator = operations()
        
    def create_widget(self):

        #widget for 1 label
        self.input1_label = Label(self, text = "Input number 1:")
        self.input1_label.grid(row=0, column=0)

        #widget for 1 entry
        self.input1 = Entry(self)
        self.input1.grid(row=0, column=1)
        
        #widget for 2 label
        self.input2_label = Label(self, text = "Input number 2:")
        self.input2_label.grid(row=1, column=0)

        #widget for 2 entry
        self.input2 = Entry(self)
        self.input2.grid(row=1, column=1)   

        #widget for operator
        self.operator_label = Label(self, text = "Operator")
        self.operator_label.grid(row=2, column=0)   

        #initial value is operator
        self.operator_var = StringVar(self)
        self.operator_var.set("Operator")

        #create a menu functions
        self.operator_options = OptionMenu(self, self.operator_var, "Addition", "Subtraction", "Multiplication", "Division")
        self.operator_options.grid(row=2, column=1)
        
        #calculations
        self.button = Button(self, text = "Click for Result!", command=self.press_button)
        
        #display result
        self.result_label = Label(self, text = '')
        self.result_label.grid(row=4, column=1)

    #We have to make press button method for buttons
    def press_button():
        #try and except for values
            #get the values


            #perform calculations

            #addition
            #subtraction
            #multiplication
            #division
            