
# This program creates a simple Unit Converter using Python’s Tkinter library.
# It allows the user to convert Celsius to Fahrenheit.

import tkinter as tk
from tkinter import messagebox

# Create the main GUI window
main_window = tk.Tk()

# Set window title
main_window.title("Celsius to Fahrenheit converter")

# Set background colour
main_window.configure(background="#CF2F24")

# Set window size
main_window.geometry("800x600")

# MAIN HEADING LABEL
label_title = tk.Label(
    main_window,
    text="Celsius to Fahrenheit converter",
    bg="white",
    fg="black",
    width=40,
    height=2,
    font=("Helvetica", 14, "bold")
)

# Position heading
label_title.place(x=150, y=40)

# -------------------- CELSIUS TO FAHRENHEIT --------------------

# Label for Celsius input
label_celsius = tk.Label(
    main_window,
    text="Enter Celsius:",
    bg="lightyellow",
    fg="black",
    width=25,
    height=2,
    font=("Helvetica", 12)
)
label_celsius.place(x=100, y=180)

# Entry box for Celsius value
entry_celsius = tk.Entry(
    main_window,
    width=30,
    bg="white",
    fg="black"
)
entry_celsius.place(x=450, y=180)

# Label to show Fahrenheit result
label_fahrenheit_result = tk.Label(
    main_window,
    text="Fahrenheit:",
    bg="lightyellow",
    fg="black",
    width=25,
    height=2,
    font=("Helvetica", 12)
)
label_fahrenheit_result.place(x=100, y=260)

# Output label for Fahrenheit
result_fahrenheit = tk.Label(
    main_window,
    text="",
    bg="white",
    fg="black",
    width=25,
    height=2
)
result_fahrenheit.place(x=450, y=260)

# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    result_fahrenheit.config(text=round(fahrenheit, 2))

# Convert button
button_convert = tk.Button(
    main_window,
    text="Convert Celsius-Fahrenheit",
    width=20,
    height=2,
    command=convert_celsius_to_fahrenheit
)
button_convert.place(x=300, y=350)

# MAIN LOOP
main_window.mainloop()




