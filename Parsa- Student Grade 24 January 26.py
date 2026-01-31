


# =========================
# TKINTER UI (Student Grading System) 

import tkinter as tk
from tkinter import messagebox


# Create the main window
main_window = tk.Tk()
main_window.title("Grade Master 3000 - v1.0")
main_window.geometry("520x420")
main_window.configure(bg="white")
main_window.resizable(False, False) # This prevents the user from resizing the window.
message = ""
def calculate_grade():     #Create a function called calculate_grade.
    global message
    roll_no = entry_roll.get()
    name = entry_name.get()
    message = name+" "+roll_no+"\n"
    maths = int(entry_math.get())
    eng = int(entry_eng.get())
    sci = int(entry_sci.get())
    total = maths+eng+sci
    percentage = (total/300)*100
    message = message+ "Your percentage is "+str(percentage)
    if percentage > 80:
        grade = "A"
    elif percentage > 70 and percentage <= 80:
        grade = "B"
    elif percentage > 60 and percentage <=70:
        grade = "C"
    message = message+"\n"+"Your grade is "+grade
    
    output_box.config(text=message)

def save_details():
    global message
    messagebox.showinfo(
        "saved","student details are saved"
    )
    file = open(r"C:\Users\Bahadori-jahromia\OneDrive - University of West London\Desktop\Jetlearn coding\Game development 2\students.txt","a")
    file.write(message)
    file.write("\n")
    file.close()
    
    
# Title
title_lbl = tk.Label(
    main_window,
    text="Student Grading System",
    bg="white",
    fg="black",
    font=("Arial", 18, "bold"),
)
title_lbl.place(x=20, y=15)

# Labels + Entry boxes
lbl_name = tk.Label(main_window, text="Name:", bg="white", fg="black", font=("Arial", 10))
lbl_name.place(x=110, y=70)
entry_name = tk.Entry(main_window, width=18, font=("Arial", 10), relief="solid", bd=1)
entry_name.place(x=190, y=68)

lbl_roll = tk.Label(main_window, text="Roll No:", bg="white", fg="black", font=("Arial", 10))
lbl_roll.place(x=110, y=95)
entry_roll = tk.Entry(main_window, width=18, font=("Arial", 10), relief="solid", bd=1)
entry_roll.place(x=190, y=93)

lbl_math = tk.Label(main_window, text="Math Marks:", bg="white", fg="black", font=("Arial", 10))
lbl_math.place(x=90, y=120)
entry_math = tk.Entry(main_window, width=18, font=("Arial", 10), relief="solid", bd=1)
entry_math.place(x=190, y=118)

lbl_sci = tk.Label(main_window, text="Science Marks:", bg="white", fg="black", font=("Arial", 10))
lbl_sci.place(x=78, y=145)
entry_sci = tk.Entry(main_window, width=18, font=("Arial", 10), relief="solid", bd=1)
entry_sci.place(x=190, y=143)

lbl_eng = tk.Label(main_window, text="English Marks:", bg="white", fg="black", font=("Arial", 10))
lbl_eng.place(x=82, y=170)
entry_eng = tk.Entry(main_window, width=18, font=("Arial", 10), relief="solid", bd=1)
entry_eng.place(x=190, y=168)

# Buttons (commands left as placeholders)
btc_calc = tk.Button(
    main_window,
    text="Calculate grade",
    bg="#FFD700",
    fg="black",
    font=("Arial", 10, "bold"),
    width=16,
    relief="raised", #Looks like it pops out or "sunken" Looks pressed in
    command =  calculate_grade
)
btc_calc.place(x=185, y=205)

btn_save = tk.Button(
    main_window,
    text="Save student",
    bg="#00D5E7",
    fg="black",
    font=("Arial", 10, "bold"),
    width=16,
    relief="raised", #Looks like it pops out
    command = save_details
)
btn_save.place(x=185, y=240)

# White output area
output_box = tk.Button(
    main_window,
    width=42,
    height=9,
    font=("Consolas", 10),
    relief="solid",
    bd=1  # bd stands for border width (in pixels).bd=1   # thin border
)
output_box.place(x=30, y=285)


main_window.mainloop()




