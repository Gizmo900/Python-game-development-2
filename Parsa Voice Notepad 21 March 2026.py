
#This Python program creates a voice-controlled notepad GUI application
#  using Tkinter and speech recognition.



import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox

# Create main window
main_window = tk.Tk()
main_window.title("Voice Notepad")
main_window.geometry("800x420")
main_window.configure(bg="black")
main_window.resizable(False, False)


# Function to recognise speech
def recognise_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source)
            text = r.recognize_google(audio)   # Convert speech to text
            text1.insert(tk.END, text + "\n")
            print("You said:", text)

        except sr.WaitTimeoutError:
            print("No speech detected within the time limit")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Request error:", e)


# Function to save text to file
def save_text():
    file = open("Output.txt", "a")      #opens a file called "Output.txt"
                                        #The "a" stands for append mode.
                                        # If the file does NOT exist → it will be created
                                        # If the file already exists → new text is added to the end

    file.write(text1.get("1.0", tk.END))  #Get all text from the beginning to the end.
                                           # "1.0" = start reading from the first word
    file.close()
    print("Text saved successfully")
    messagebox.showinfo("Success", "Text saved successfully")
    

# Function to clear text box
def clear_text():
    text1.delete("1.0", tk.END)


# Button to start recording
Button1 = tk.Button(
    text="Click me to start recording",
    width=25,
    height=3,
    bg="blue",
    fg="white",
    command=recognise_speech
)
Button1.place(x=50, y=150)


# Text box
text1 = tk.Text(width=40, height=8, font=("Arial", 12))
text1.place(x=250, y=130)


# Save button
Button2 = tk.Button(
    text="Save text",
    width=20,
    height=2,
    bg="red",
    fg="white",
    command=save_text
)
Button2.place(x=600, y=150)


# Clear button
Button3 = tk.Button(
    text="Clear",
    width=20,
    height=2,
    bg="yellow",
    command=clear_text
)
Button3.place(x=600, y=200)


# Run the window
main_window.mainloop()












