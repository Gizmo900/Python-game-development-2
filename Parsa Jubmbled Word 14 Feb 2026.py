
#This program creates a simple Tkinter riddle game where a question is shown,
# the correct answer is jumbled, and the user types their guess 
# to be checked as correct or wrong.

import tkinter as tk
from tkinter import messagebox
import random


riddles = {"What has a head and a tail but no body?":"coin",
           "What has to be broken before you can use it?":"egg",
           "What is full of holes but can still hold water?":"sponge",
           "What goes up when the rain comes down?":"umbrella",
           "What has one eye, but cannot see?":"needle"}

# Select first question
first_question = next(iter(riddles))
answer = riddles[first_question]

current_key = first_question


#second_question = next(iter(riddles))
#answer = riddles[second_question]

#third_question = next(iter(riddles))
#answer = riddles[third_question]

#fourth_question = next(iter(riddles))
#answer = riddles[fourth_question]

#fifth_question = next(iter(riddles))
#answer = riddles[fifth_question]

#Jumble the answers
jumbled_answer = list(answer)
random.shuffle(jumbled_answer)
jumbled_word = "".join(jumbled_answer) #Joins all the letters in the list into one single word (string)
                                       #"" means join with nothing between the letters

# Function to check answer
def check_answer():
    user_answer = e1.get().lower().strip() #Gets whatever the user typed into the entry box
                                           #converts everyting to lowercase
                                           #Removes extra spaces at the beginning and end.
    if user_answer==answer:
        result_label.config(text = "Your answer is correct!", fg = "green")
    else:
        result_label.config(text = "Your answer is wrong!", fg = "red")

def next_question():
    global riddles,current_key, answer
    e1.delete(0,tk.END)
    e1.insert(0,"")
    keys = list(riddles.keys())
    current_index = keys.index(current_key)
    if current_index==4:
        messagebox.showinfo("Done","There are no more riddles")
    else:
        second_question = keys[current_index+1]
        answer = riddles[second_question]
        question_label.config(text = second_question)
        current_key = second_question
        answer = riddles[second_question]
        jumbled_answer = list(answer)
        random.shuffle(jumbled_answer)
        jumbled_word = "".join(jumbled_answer) 
        jumble_label.config(text = jumbled_word)

# Create window
main_window = tk.Tk()
main_window.title("Jumbled word")
main_window.geometry("520x420")
main_window.configure(bg = "black")
main_window.resizable(False,False)

#Question label
question_label = tk.Label(main_window, text = first_question,
                          bg = "white", fg = "black", font = ("Arial", 15))
question_label.place(x = 100, y = 50)

# Jumbled word label
jumble_label = tk.Label(main_window, text = jumbled_answer,
                          bg = "white", fg = "black", font = ("Arial", 15))
jumble_label.place(x = 100, y = 100)

#Entry box
e1 = tk.Entry(width = 30, bg = "white")
e1.place(x = 100, y = 150)

#Button
start_button = tk.Button(main_window, text = "Check Answer",
                         bg = "white", fg = "black",
                         font = ("Arial", 15),
                         command = check_answer)
start_button.place(x = 100, y = 230)

#Result label
result_label = tk.Label(main_window, text = "",
                        bg = "black", fg = "white", font = ("Arial", 15))
result_label.place(x = 50, y = 300)

next_button = tk.Button(main_window, text = "Next",
                         bg = "white", fg = "black",
                         font = ("Arial", 15),
                         command = next_question)
next_button.place(x = 300, y = 230)
main_window.mainloop()









