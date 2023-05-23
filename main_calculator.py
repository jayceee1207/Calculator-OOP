#import tkinter for window
from tkinter import *

#import Tkinter GUI interface
from TkinterGUI import UserInterface


# Create the window
window = Tk()
window.title("My Simple Calculator")
window.geometry("500x200")


# Call the User Interface
app = UserInterface(window)

window.mainloop()


