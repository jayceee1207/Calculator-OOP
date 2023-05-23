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

        #initial value is operator

        #create a menu functions

        #calculations

        #display result