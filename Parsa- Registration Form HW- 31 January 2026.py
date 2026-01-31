

import tkinter as tk
from tkinter import messagebox  #imports the pop-up dialog tools from Tkinter — 
                               #the little windows that show:
                               # information, warnings, errors, questions

# Create the main window
main_window = tk.Tk()
main_window.title("Registration Master 3000 - v1.0")
main_window.geometry("420x320")
main_window.configure(bg="white")
main_window.resizable(False, False) # This prevents the user from resizing the window.

BG = "#F7F2D8"
main_window.configure(bg=BG)

#------Variables-------
full_name_var = tk.StringVar()
email_var = tk.StringVar()

gender_var = tk.StringVar(value = "")
country_var = tk.StringVar(value = "select your country")

java_var = tk.IntVar(value=0)
python_var = tk.IntVar(value=0)

#---------Action-------
def submit_form():
    name = full_name_var.get().strip()
    email = email_var.get().strip()
    gender = gender_var.get().strip()
    country = country_var.get().strip()

    languages = []
    if java_var.get():
        languages.append("Java")
    if python_var.get():
        languages.append("Python")

# ---- Validation ----
    if not name:
        messagebox.showwarning("Missing field", "Please enter your full name.")
        return
    if not email or "@" not in email:
        messagebox.showwarning("Missing field", "Please enter a valid email.")
        return
    if gender not in ("Male", "Female"):
        messagebox.showwarning("Missing field", "Please select your gender.")
        return
    if country == "select your country":
        messagebox.showwarning("Missing field", "Please select your country.")
        return

    # ---- Summary ----
    summary = (
        f"Full Name: {name} \n"
        f"Email: {email}\n"
        f"Gender: {gender}\n"
        f"Country: {country}\n"
        f"Programming: {', '.join(languages) if languages else None}"
    )

    messagebox.showinfo("Submitted", summary)

#------Title------
title_lbl = tk.Label(
    main_window,
    text="Registration form",
    bg = BG,
    fg = "black",
    font = ("Arial", 18, "bold")
)
title_lbl.place(x=210, y=35, anchor = "center")

#------Full name------
tk.Label(main_window, text ="FullName", bg = BG, font = ("Arial, 9")).place(x=110, y = 95)
tk.Entry(main_window,textvariable=full_name_var, width = 18, relief = "solid", bd = 1).place(x=210, y=93)

# ---------- Email ----------
tk.Label(main_window, text="Email", bg=BG, font=("Arial", 9)).place(x=110, y=130)
tk.Entry(main_window, textvariable=email_var, width=18, relief="solid", bd=1).place(x=210, y=128)

# ---------- Gender ----------
tk.Label(main_window, text = "Gender", bg=BG, font=("Arial", 9)).place(x=110, y=165)
tk.Radiobutton(main_window,text = "Male", value = "Male", variable = gender_var, bg=BG).place(x=210, y=159)
tk.Radiobutton(main_window,text = "Female", value = "Female", variable = gender_var, bg=BG).place(x=280, y=159)

# ---------- Country ----------
tk.Label(main_window, text="Country", bg=BG, font=("Arial", 9)).place(x=110, y=200)

countries = ["UK", "Iran", "Greece", "USA", "Canada", "Germany", "France", "India"]
country_menu = tk.OptionMenu(main_window, country_var, *countries)
country_menu.configure(bg="white", relief="solid", bd=1, width=16)
country_menu["menu"]. configure(bg = "white")
country_menu.place(x = 208, y = 192)

# ---------- Programming ----------
tk.Label(main_window, text="Programming", bg=BG, font=("Arial", 9)).place(x=110, y=235)
tk.Checkbutton(main_window, text="java", variable = java_var, bg=BG).place(x = 210, y = 229)
tk.Checkbutton(main_window, text="python", variable = python_var, bg=BG).place(x = 280, y = 229)

# Buttons (commands left as placeholders)
submit_btn = tk.Button(
    main_window,
    text="Submit",
    bg="#B21717",
    fg="white",
    font=("Arial", 10, "bold"),
    width=18,
    relief="raised", #Looks like it pops out or "sunken" Looks pressed in
    command = submit_form
) 
submit_btn.place(x=210, y=300, anchor = "center")


main_window.mainloop()





