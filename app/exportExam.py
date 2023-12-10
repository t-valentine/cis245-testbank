from tkinter import *
import tkinter.messagebox as msg

# Switch to exam export page
def switch_to_exportExam():
    ws.destroy()
    # this should have the API call
    import exportExam

def logout():
    ws.destroy()
    import login

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

def button_clicked():
    """
    This function will help display error messages
    """
    msg.showerror("Error")


# Initiate GUI

ws = Tk()
ws.title("CIS 245 Testbank Application")
ws.geometry("500x500")
ws.columnconfigure(5)


frame = Frame(ws)

# Creating Labels
Label(frame, text="Created Exam", padx=15, pady=15).grid(row=0, column=2, sticky=W)

# Creating Generate Exam button
exportExam_button = Button(frame, text="Export Exam", command=button_clicked, cursor="mouse")
exportExam_button.bind("<Return>", lambda event: button_clicked())

# Creating Log Out button
logout_button = Button(frame, text="Log Out", command=logout, cursor="mouse")
logout_button.bind("<Return>", lambda event: logout())


# Placement of text boxes and buttons
logout_button.grid(row=0, column=0, padx=10, pady=10)
exportExam_button.grid(row=2, column=1, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()