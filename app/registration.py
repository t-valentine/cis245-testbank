from tkinter import *
import regex as re
import mysql.connector
import argon2
import tkinter.messagebox as msg

def switch_to_login():
    """
    This function destroys and then switches to the login screen.
    """
    import login
    ws.destroy()
    login

def display_error(message):
    """
    This function will help display error messages
    """
    msg.showerror("Error", message)

def clear_form():
    """
    This funciton will clear the form.
    """
    register_email.delete(0, END)
    confirm_email.delete(0, END)
    register_password.delete(0, END)

def email_validator(email, email2):
    """
    This function will check for the following things using regular expression:
    - That the email is following the proper format.
    - That the email and the confirmation email match.
    """
    if email == email2:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return None
        else:
            return "Invalid email format"
    else:
        return "Emails do not match"

def password_validator(password):
    """
    This function will validate the password with minimum standards, using regular expression:
    - Password must be at least 8 characters.
    - Password must include at least one special character.
    - Password must include at least one number.
    - Password must be less than 50 characters.
    """
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

def user_exists(email):
    """
    Checks if a user with the given email is already existing in the database.
    """
    try:
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        cursor.execute(query, (email, ))
        result = cursor.fetchone()[0]
        return result > 0
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        conn.rollback()
        return False

def insert_user(email, password):
    """
    This function will insert users into email and password database.
    """
    try:
        if user_exists(email):
            display_error("Account already exists")
            return False
        else:
            query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(query, (email, password))
            conn.commit()
            return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        conn.rollback()
        return False

def submit():
    """
    This function will submit the registatrion form,
    Hash the password using argon2, and
    it will notify user if registration was succesful or not.
    """
    email = register_email.get()
    password = register_password.get()

    email_error = email_validator(email, confirm_email.get())
    password_error = password_validator(password)

    if email_error or password_error:
        if email_error:
            display_error(email_error)
        if password_error:
            display_error(password_error)
        return False
    else:
        hashed_password = password_hasher.hash(password)  # hashes the password

        if insert_user(email, hashed_password):
            msg.showinfo("Success", "Registration Successful")
            switch_to_login()
            return True
        else:
            display_error("Failed to register")
            return False
        
# Database Integration
try:
    conn = mysql.connector.connect(
        host="localhost",  # hostname
        user="<user>",  # username
        password="<password>",  # password
        database="testbank",  # database name
    )  # please note the information above will need to be changed according the database in use

    cursor = conn.cursor()
except mysql.connector.Error as err:
    display_error(f"Database error: {err}")
    conn.rollback()

# Argon2 password hasher
password_hasher = argon2.PasswordHasher()

# Initiate GUI
ws = Tk()
ws.title("Sign-up Page")
ws.geometry("400x200")

frame = Frame(ws, relief=SOLID, bd=2, padx=10, pady=10)

# Creating Labels
Label(frame, text="Email:", padx=5, pady=5).grid(row=0, column=0, sticky=W)
Label(frame, text="Confirm Email:", padx=5, pady=5).grid(row=1, column=0, sticky=W)
Label(frame, text="Password:", padx=5, pady=5).grid(row=2, column=0, sticky=W)

# Creating text boxes
register_email = Entry(frame)
confirm_email = Entry(frame)
register_password = Entry(frame, show="*")

# Creating register button
register_button = Button(frame, text="SignUp", command=submit, cursor="mouse")
register_button.bind("<Return>", lambda event: submit())

# Creating clear button
clear_button = Button(frame, text="Clear", command=clear_form, cursor="mouse")
clear_button.bind("<Return>", lambda event: clear_form())

# Placement of text boxes and buttons
register_email.grid(row=0, column=1, padx=5, pady=5)
confirm_email.grid(row=1, column=1, padx=5, pady=5)
register_password.grid(row=2, column=1, padx=5, pady=5)
register_button.grid(row=4, column=1, padx=10, pady=10)
clear_button.grid(row=4, column=0, padx=10, pady=10)

# Creating the hyperlink to the login page
login_link = Label(
    frame,
    text="Already have an account? Follow the link to login",
    fg="blue",
    cursor="hand2",
)
login_link.grid(row=5, column=0, columnspan=2, pady=10)
login_link.bind("<Button-1>", lambda event: switch_to_login())
login_link.bind("<Return>", lambda event: switch_to_login())

# Show the registration page
frame.pack()

# Validate the email, and password
validated_email = ws.register(email_validator)
validated_password = (ws.register(password_validator), "%P")

register_email.config(
    validate="key", validatecommand=(email_validator, "%P", confirm_email.get())
)
register_password.config(validate="key", validatecommand=(password_validator, "%P"))

# Start the tkinter event
if __name__ == "__main__":
    ws.mainloop()
