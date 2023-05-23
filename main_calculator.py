#import Tkinter GUI interface
from TkinterGUI import UserInterface

#import tkinter for window
from tkinter import *

# Create the window
window = Tk()
window.title("Simple Calculator")
window.geometry("400x200")

# Call the User Interface
app = UserInterface(window)

window.mainloop()


