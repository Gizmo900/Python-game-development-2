
# This program creates a simple Unit Converter using Python’s Tkinter library.
# It allows the user to convert inches to centimetres.

import tkinter as tk
from tkinter import messagebox

# Create the main GUI window
main_window = tk.Tk()

# Set window title
main_window.title("Inches to Centimeters converter")

# Set background colour
main_window.configure(background="#6FA8DC")

# Set window size
main_window.geometry("800x600")

# MAIN HEADING LABEL
label_title = tk.Label(
    main_window,
    text="Inches to Centimeters converter",
    bg="white",
    fg="black",
    width=40,
    height=2,
    font=("Helvetica", 14, "bold")
)

# Position heading
label_title.place(x=150, y=40)

# -------------------- INCH TO CM --------------------

# Label for inches input
label_inch = tk.Label(
    main_window,
    text="Enter inches:",
    bg="lightyellow",
    fg="black",
    width=25,
    height=2,
    font=("Helvetica", 12)
)
label_inch.place(x=100, y=180)

# Entry box for inches value
entry_inch = tk.Entry(
    main_window,
    width=30,
    bg="white",
    fg="black"
)
entry_inch.place(x=450, y=180)

# Label to show centimeters result
label_cm_result = tk.Label(
    main_window,
    text="Centimeters:",
    bg="lightyellow",
    fg="black",
    width=25,
    height=2,
    font=("Helvetica", 12)
)
label_cm_result.place(x=100, y=260)

# Output label for centimeters
result_cm = tk.Label(
    main_window,
    text="",
    bg="white",
    fg="black",
    width=25,
    height=2
)
result_cm.place(x=450, y=260)

# Function to convert inches to centimeters
def convert_inch_to_cm():
    inches = float(entry_inch.get())
    cm = inches * 2.54
    result_cm.config(text=round(cm, 2))

# Convert button
button_convert = tk.Button(
    main_window,
    text="Convert inch-cm",
    width=20,
    height=2,
    command=convert_inch_to_cm
)
button_convert.place(x=300, y=350)

# MAIN LOOP
main_window.mainloop()
