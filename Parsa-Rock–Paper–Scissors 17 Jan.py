
# This program creates a simple Rock–Paper–Scissors game using Python’s Tkinter library 
#(Python’s Tkinter library is used for making graphical user interfaces). 




# Import tkinter for GUI
import tkinter as tk

# Import messagebox (for pop-up messages)
from tkinter import messagebox

# Import random for computer's random choice
import random

# Function that runs when a button is clicked
def rps(playerchoice):
    # List of choices for the computer
    computeroption = ["rock", "paper", "scissors"]
    
    # Randomly choose one option
    computerchoice = random.choice(computeroption)
    
    # Display player's choice
    labelP.config(text="You chose: " + playerchoice)
    
    # Display computer's choice
    labelC.config(text="Computer chose: " + computerchoice)
    result=""
    if computerchoice==playerchoice:
        result="its a tie"
    elif computerchoice=="rock":
        if playerchoice=="paper":
            result="Player Wins"
        if playerchoice=="scissors":
            result="Computer wins"
    elif computerchoice=="paper":
        if playerchoice=="rock":
            result="Computer wins"
        if playerchoice=="scissors":
            result="Player wins"
    elif computerchoice=="scissors":
        if playerchoice=="rock":
            result="Player wins"
    elif computerchoice=="scissors":
        if playerchoice=="paper":
            result="Computer wins"
    labelR.config(text=result)



# Create the main window
gui = tk.Tk()

# Set the window title
gui.title("Rock Paper Scissors")

# Set background colour
gui.configure(background="#149A7B")

# Set window size
gui.geometry("800x800")

# Create the title label
label1 = tk.Label(
    text="Rock Paper Scissors",
    bg="white",
    fg="black", #fg = text colour
    width=30,
    height=2,
    font=("Helvetica", 12, "bold italic underline")
)

# Position the title label
label1.place(x=200, y=50)

# Create label for options section
label2 = tk.Label(
    text="Your options",
    bg="white",
    fg="black",
    width=20,
    height=2,
    font=("Helvetica", 12, "bold italic underline")
)

# Position the options label
label2.place(x=50, y=150)

# Create Rock button
button1 = tk.Button(
    text="Rock",
    width=20,
    height=2,
    bg="yellow",
    command=lambda: rps("rock")  # Calls function with "rock"
)                                #lambda creates a small waiting function
                                 # it tells Python: "Only run rps ("rock")when the button is clicked"
button1.place(x=300, y=150)

# Create Paper button
button2 = tk.Button(
    text="Paper",
    width=20,
    height=2,
    bg="blue",
    command=lambda: rps("paper")  # Calls function with "paper"
)
button2.place(x=450, y=150)

# Create Scissors button
button3 = tk.Button(
    text="Scissors",
    width=20,
    height=2,
    bg="red",
    command=lambda: rps("scissors")  # Calls function with "scissors"
)
button3.place(x=600, y=150)

# Label to show player's choice
labelP = tk.Label(
    text="You chose:",
    bg="white",
    fg="black",
    width=20,
    height=2,
    font=("Helvetica", 12, "bold italic")
)
labelP.place(x=100, y=250)

# Label to show computer's choice
labelC = tk.Label(
    text="Computer chose:",
    bg="white",
    fg="black",
    width=20,
    height=2,
    font=("Helvetica", 12, "bold italic")
)
labelC.place(x=400, y=250)

# Label to show the result (win/lose/draw)
labelR = tk.Label(
    text="Result:",
    bg="white",
    fg="black",
    width=20,
    height=2,
    font=("Helvetica", 12, "bold italic underline")
)
labelR.place(x=200, y=350)

# Keep the window running
gui.mainloop()
