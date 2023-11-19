from tkinter import *
import regex as re
import mysql.connector
import argon2
import tkinter.messagebox as msg
import registration
import generateExam

# Database Integration
conn = mysql.connector.connect(
    host="localhost",  # hostname
    user="Torres",  # username
    password="Test123!",  # password
    database="testbank",  # database name
)  # please note the information above will need to be changed according the database in use

cursor = conn.cursor()


def button_clicked():
    """
    This function will submit the registatrion form,
    Hash the password using argon2, and
    it will notify user if registration was succesful or not.
    """
    email = email_input.get()
    password = password_input.get()


subject = [
"Geology",
"Computer Information Systems",
"Math"
] 

difficulty = [
"Easy",
"Medium",
"Hard"
] 

question_format = [
"True/False",
"Multiple Choice",
"Multi-Answer",
"Fill-in-the-Blank"
] 

# Initiate GUI
ws = Tk()
ws.title("Log-In Page")
ws.geometry("400x200")

frame = Frame(ws, relief=SOLID, bd=2, padx=10, pady=10)

# Creating Labels
Label(frame, text="Subject:", padx=5, pady=5).grid(row=0, column=0, sticky=W)
Label(frame, text="Difficulty:", padx=5, pady=5).grid(row=1, column=0, sticky=W)
Label(frame, text="Number of Questions:", padx=5, pady=5).grid(row=2, column=0, sticky=W)
Label(frame, text="Question Formats:", padx=5, pady=5).grid(row=3, column=0, sticky=W)


# Creating Dropdowns
subjects = StringVar(ws)
subjects.set(subject[0])
subject_input = OptionMenu( ws , subjects , *subject )
difficulties = StringVar(ws)
difficulties.set(difficulty[0])
difficulty_input = OptionMenu( ws , difficulties , *difficulty ) 
formats = StringVar(ws)
formats.set(format[0])
format_input = OptionMenu( ws , formats , *format ) 

# Creating entry for # of questions
questionnumber_input = Entry(frame)

# Creating Generate Exam button
generateExam_button = Button(frame, text="Generate Exam", command=button_clicked, cursor="mouse")
generateExam_button.bind("<Return>", lambda event: button_clicked())

# Creating Log Out button
logout_button = Button(frame, text="Log Out", command=button_clicked, cursor="mouse")
logout_button.bind("<Return>", lambda event: button_clicked())


# Placement of text boxes and buttons
logout_button.grid(row=0, column=1, padx=10, pady=10)
subject_input.grid(row=1, column=1, padx=10, pady=10)
difficulty_input.grid(row=2, column=1, padx=10, pady=10)
questionnumber_input.grid(row=3, column=1, padx=5, pady=5)
format_input.grid(row=4, column=1, padx=10, pady=10)
generateExam_button.grid(row=5, column=1, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()
