

#This program creates a simple digital clock window with a title, a button, and a space to display time.
#  When the user clicks “Show time”, it gets the current system time.


import tkinter as tk
from datetime import datetime
#Imports datetime to get the current time


# Create the main window
main_window = tk.Tk()
main_window.title("Digital clock")
main_window.geometry("520x420")
main_window.configure(bg="white")
main_window.resizable(False, False) # This prevents the user from resizing the window.

# Creates a title label
Lb_title = tk.Label(main_window, text="Digital clock", bg="white", fg="black", font=("Arial", 15))
Lb_title.place(x=100, y=50)

# Creates a label to show the time
result_label = tk.Label(main_window, text="", bg="white", fg="black", font=("Arial", 15))
result_label.place(x=100, y=150)

result_label2 = tk.Label(main_window, text="", bg="white", fg="black", font=("Arial", 15))
result_label2.place(x=100, y=250)

def show_current_time():
    # Defines a function to show the time

    current_time = datetime.now().strftime("%H:%M:%S")
    # Gets the current time of hours, minutes and seconds

    result_label.config(text = current_time)
    # Updates the label with the current time

    result_label.after(1000, show_current_time)

def show_current_date():
    current_date = datetime.now().strftime("%d/%B/%Y")
    result_label2.config(text = current_date)
    # Updates the label with the current time

    result_label2.after(3600000, show_current_date)


# Creates a button
show_time = tk.Button(

    main_window,# Adds button to the main window
    
    text = "Show time", # button text

    bg = "blue",

    fg = "white",

    font = ("Arial", 15),

    command = show_current_time
    # Runs the function when clicked
)

show_time.place(x = 100, y = 100)

show_date = tk.Button(

    main_window,# Adds button to the main window
    
    text = "Show date", # button text

    bg = "blue",

    fg = "white",

    font = ("Arial", 15),

    command = show_current_date
)
show_date.place(x = 100, y = 200)
main_window.mainloop()
# Keeps the window running




