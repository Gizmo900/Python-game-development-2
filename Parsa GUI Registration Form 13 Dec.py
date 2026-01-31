
#  Main heading: Registration Form
#  Two labels: Enter your name and Enter your age
#  Two entry boxes next to each label
#  A Submit button at the bottom
#  Clean layout using .place()

import tkinter as tk
from tkinter import messagebox
gui = tk.Tk()

gui.title("Registration Homework")

gui.configure(background="#149A7B")

gui.geometry("800x800")

# Main heading label
label_title = tk.Label(
    text = "Registration",
    bg = "white",
    fg = "black",
    width = 40,
    height = 2,
    font = ("Helvetica", 12, "bold italic underline")
)

label_title.place(x = 150, y = 50)

# Label 1 - Enter your name
label_name = tk.Label(
    text="Enter your name:",
    bg="red",
    fg="blue",
    width=20,
    height=2,
    font=("Helvetica", 12)
)
label_name.place(x=150, y=150)




# Label 2 - Enter your age
label_name2 = tk.Label(
    text="Age:",
    bg="red",
    fg="blue",
    width=20,
    height=2,
    font=("Helvetica", 12)
)
label_name2.place(x= 150, y=250)






# Entry box for name
entry_name = tk.Entry(
    width=30,
    bg="white",
    fg="black"
)# Entry box for name
entry_name.place(x=500, y=150)

# Entry box for age
entry_age = tk.Entry(
    width=30,
    bg="white",
    fg="black"
)# Entry box for age
entry_age.place(x=500, y=250)





# Submit button
button_submit = tk.Button(
    text="Submission",
    bg="white",
    fg="black",
    width=15,
    height=2
)

button_submit.place(x=300, y=650)     

 #Label 2 - Enter your age
label_name3 = tk.Label(
    text="Select your gender:",
    bg="red",
    fg="blue",
    width=20,
    height=2,
    font=("Helvetica", 12)
)
label_name3.place(x= 150, y=350)

radiobutton1 = tk.Radiobutton(value = "male", name = "male", text = "male")
radiobutton1.place (x = 450, y = 350)

radiobutton2 = tk.Radiobutton(value = "female", name = "female", text = "female")
radiobutton2.place (x = 600, y = 350)

label_name4 = tk.Label(
    text="Select your hobbies:",
    bg="red",
    fg="blue",
    width=20,
    height=2,
    font=("Helvetica", 12)
)
label_name4.place(x= 150, y=450)

checkbox1 = tk.Checkbutton(text="coding", onvalue=1, offvalue=0 )
checkbox1.place(x = 450, y = 450)

checkbox2 = tk.Checkbutton(text="swimming", onvalue=1, offvalue=0 )
checkbox2.place(x = 550 , y = 450)

checkbox3 = tk.Checkbutton(text="badminton", onvalue=1, offvalue=0 )
checkbox3.place(x = 650, y = 450)

checkbox4 = tk.Checkbutton(text="reading", onvalue=1, offvalue=0 )
checkbox4.place(x = 750, y = 450)

list1 = ["Maths", "English", "Science", "History", "D.T", "Drama"]
value_inside = tk.StringVar(gui)

# Set the default value of the variable
value_inside.set("Select an Option")
dropdown1 = tk.OptionMenu(gui,value_inside,*list1)
dropdown1.place(x = 450, y = 550)

label_name5 = tk.Label(
    text="Select your favourite subject:",
    bg="red",
    fg="blue",
    width=20,
    height=2,
    font=("Helvetica", 12)
)
label_name5.place(x= 150, y=550)

gui.mainloop()       # Runs the GUI loop    




