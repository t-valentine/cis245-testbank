from tkinter import *
import tkinter.messagebox as msg


# Swith to exam generation page link
def switch_to_generateExam():
    ws.destroy()
    import generateExam


# Immediate Feedback on Errors
def display_error(message):
    """
    This function will help display error messages
    """
    msg.showerror("Error", message)


def login_validation():
    email = email_input.get()
    password = password_input.get()

    if email and password:
        # Verifies that username & password match
        # Right now there's no additional validation or seperate errors for a missing username/password
        if email == "test@gmail.com" and password == "password":
            switch_to_generateExam()
        else:
            display_error("Incorrect email and/or password")
    

def load_registration():
    ws.destroy()
    import generateExam


# Initiate GUI
ws = Tk()
ws.title("CIS 245 Testbank Application")
ws.geometry("500x500")

frame = Frame(ws)

# Creating Labels
Label(frame, text="Log In", padx=15, pady=15).grid(row=0, column=0, sticky=W)
Label(frame, text="Email:", padx=5, pady=5).grid(row=1, column=0, sticky=W)
Label(frame, text="Password:", padx=5, pady=5).grid(row=2, column=0, sticky=W)

# Creating text boxes
email_input = Entry(frame)
password_input = Entry(frame, show="*")

# Creating login button
login_button = Button(frame, text="Log In", command= login_validation, cursor="mouse")
login_button.bind("<Return>", lambda event: login_validation)
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