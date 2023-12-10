from tkinter import *
import tkinter.messagebox as msg


# Switch to exam generation page
def switch_to_generateExam():
    ws.destroy()
    import generateExam

# Switch to registration page
def load_registration():
    ws.destroy()
    import registration


# Immediate Feedback on Errors
def display_error(message):
    msg.showerror("Error", message)

# Verifies that username & password match
# Right now there's no additional validation or seperate errors for a missing username/password
def login_validation(email, password):
    if not email and not password:
        return "No user input"
    elif not email and password:
        return "No email"
    elif email and not password:
        return "No password"
    if email and password:
        # Here is where we would validate login against the database
        if (email == "test@gmail.com" and password == "password") or (email == "test" and password == "p") :
            return "Valid"

def login():
    email = email_input.get()
    password = password_input.get()
    validateLogin = login_validation(email, password)
    match validateLogin:
        case "Valid":
            switch_to_generateExam()
        case "Invalid":
            display_error("Incorrect email and/or password")
        case "No email":
            display_error("Enter an email address to login")
        case "No password":
            display_error("Enter a password to login")
        case "No user input":
            display_error("Enter an username and password to login")
        case _:
            display_error("Incorrect email and/or password")

# Initiate GUI
ws = Tk()
ws.title("CIS 245 Testbank Application")
ws.geometry("500x500")

frame = Frame(ws)

# Creating Labels
Label(frame, text="Log In", padx=15, pady=15).grid(row=0, column=1)
Label(frame, text="Email:", padx=5, pady=5).grid(row=1, column=0, sticky=W)
Label(frame, text="Password:", padx=5, pady=5).grid(row=2, column=0, sticky=W)

# Creating text boxes
email_input = Entry(frame)
password_input = Entry(frame, show="*")

# Creating login button
login_button = Button(frame, text="Log In", command= login, cursor="mouse")
login_button.bind("<Return>", lambda event: login)
registration_button = Button(frame, text="Create Account", command= load_registration, cursor="mouse")
registration_button.bind("<Return>", lambda event: load_registration)


# Placement of text boxes and buttons
email_input.grid(row=1, column=1, padx=5, pady=5)
password_input.grid(row=2, column=1, padx=5, pady=5)
login_button.grid(row=3, column=1, padx=10, pady=10)
registration_button.grid(row=4, column=1, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()