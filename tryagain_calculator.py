#import tkinter messagebox
from tkinter import messagebox
#create a class try again
class TryAgain:
    #attributes for the class
    def __init__ (self, root, result_button, number1_entry, number2_entry):
        self.root = root
        self.result_button = result_button
        self.number1_entry = number1_entry
        self.number2_entry = number2_entry
    
    #function for messagebox
    def ask(self):   
        #ask user
        moredata = moredata.askquestion("Do you want to try again?")
        #if answer is yes
        if moredata == "Yes":
            #the program will rerun
            self.result_button.config(text="Result")
            self.number1_entry.delete(0, "end")
            self.number2_entry.delete(0, "end")
        #else
            #the program will end
            messagebox.showinfo("Thank you for using the calculator!")
            self.root.destroy()