import mysql.connector
from tkinter import *
import tkinter.messagebox as msg
from argon2 import PasswordHasher

password_hasher = PasswordHasher()

def display_error(message):
    """
    This function will help display error messages
    """
    msg.showerror("Error", message)

def validate_login(email, password):
    """
    This function will validate login by checking if in database
    """
    try:
        # TODO: Change connection to correct Database
        # Database Integration
        conn = mysql.connector.connect(
            host="localhost",  # hostname
            user="<user>",  # username
            password="<password>",  # password
            database="testbank",  # database name
        )  # please note the information above will need to be changed according the database in use
        cursor = conn.cursor()
        user_email = (email, )
        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, user_email)
        user = cursor.fetchone()
        if user:
            hashed_password_from_database = str(user[0])
            try:
                password_hasher.verify(hashed_password_from_database, password)
                return True
            except:
                return False
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()
    return False

def submit():
    """
    This function will submit the login form,
    and notify user if login was successful or not.
    """
    user_email = email.get()
    user_password = password.get()

    login_validation = validate_login(user_email, user_password)

    if login_validation == True:
        msg.showinfo("Success", "Login Succesful")
        switch_to_home_page()
    else:
        display_error("Failed to login")

def switch_to_home_page():
    """
    This function will switch take the user to the Home page and close the login window.
    """
    ws.destroy()
    # TODO: import home/landing page 
    # home/landing page

def clear_form():
    """
    This funciton will clear the form.
    """
    email.delete(0, END)
    password.delete(0, END)


def go_to_register():
    """
    This funciton will allow the user to go to the registration page and destroy the login window.
    """
    import registration
    ws.destroy()
    registration

# Initiate GUI
ws = Tk()
ws.title("Login Page")
ws.geometry("400x200")

frame = Frame(ws, relief=SOLID, bd=2, padx=10, pady=10)

# Creating Labels
Label(frame, text="Email:", padx=5, pady=5).grid(row=0, column=0, sticky=W)
Label(frame, text="Password:", padx=5, pady=5).grid(row=1, column=0, sticky=W)

# Creating text boxes
email = Entry(frame)
password = Entry(frame, show="*")

# Create Login button
login_button = Button(frame, text="Login", command=submit, cursor="mouse")
login_button.bind("<Return>", lambda event: submit())

# Creating clear button
clear_button = Button(frame, text="Clear", command=clear_form, cursor="mouse")
clear_button.bind("<Return>", lambda event: clear_form())

# Place text boxes
email.grid(row=0, column=1, padx=5, pady=5)
password.grid(row=1, column=1, padx=5, pady=5)

# Place buttons
login_button.grid(row=2, column=0, padx=5, pady=5)
clear_button.grid(row=2, column=1, padx=5, pady=5)

# Create hyperlink to sign up page
register_link = Label(
    frame,
    text="Need to register? Click here!",
    fg="blue",
    cursor="hand2",
)

# Hyperlink placement and attaching left-click and return
register_link.grid(row=3, column=0, columnspan=2, pady=10)
register_link.bind("<Button-1>", lambda event: go_to_register())
register_link.bind("<Return>", lambda event: go_to_register())

# Show the login page
frame.pack()

# Start the tkinter event
if __name__ == "__main__":
    ws.mainloop()
