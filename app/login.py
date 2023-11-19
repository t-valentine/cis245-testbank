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

# Argon2 password hasher
password_hasher = argon2.PasswordHasher()


# Swith to registration page link
def switch_to_registration():
    registration

# Swith to exam generation page link
def switch_to_generateExam():
    generateExam


# Immediate Feedback on Errors
def display_error(message):
    """
    This function will help display error messages
    """
    msg.showerror("Error", message)

# Verifies that username & password match
def login_validator(email, password):
    if len(password) >= 8:
        if (
            re.search(r"[!@#$%^&*()_+]", password)
            and re.search(r"\d", password)
            and len(password) <= 50
        ):
            return None
        else:
            return "Password must include at least one special character and one number and cannot be longer than 50 characters."
    else:
        return "Password must be at least 8 characters."


def button_clicked():
    """
    This function will submit the registatrion form,
    Hash the password using argon2, and
    it will notify user if registration was succesful or not.
    """
    email = email_input.get()
    password = password_input.get()

    login_error = login_validator(email, password)

    if login_error:
        display_error(login_error)
    else:
        # navigate to generateExam.py
        display_error(login_error)


# Initiate GUI
ws = Tk()
ws.title("Log-In Page")
ws.geometry("400x200")

frame = Frame(ws, relief=SOLID, bd=2, padx=10, pady=10)

# Creating Labels
Label(frame, text="Email:", padx=5, pady=5).grid(row=0, column=0, sticky=W)
Label(frame, text="Password:", padx=5, pady=5).grid(row=1, column=0, sticky=W)

# Creating text boxes
email_input = Entry(frame)
password_input = Entry(frame, show="*")

# Creating login button
login_button = Button(frame, text="Log In", command=button_clicked, cursor="mouse")
login_button.bind("<Return>", lambda event: button_clicked())


# Placement of text boxes and buttons
email_input.grid(row=0, column=1, padx=5, pady=5)
password_input .grid(row=1, column=1, padx=5, pady=5)
login_button.grid(row=3, column=1, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()
