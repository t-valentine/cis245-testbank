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


frame = Frame(ws)

# Creating Labels
Label(frame, text="Generate Exam", padx=15, pady=15).grid(row=0, column=1, sticky=W)
Label(frame, text="Subject:", padx=5, pady=5).grid(row=1, column=0, sticky=W)
Label(frame, text="Difficulty:", padx=5, pady=5).grid(row=2, column=0, sticky=W)
Label(frame, text="Number of Questions:", padx=5, pady=5).grid(row=3, column=0, sticky=W)
Label(frame, text="Question Formats:", padx=5, pady=5).grid(row=4, column=0, sticky=W)

# Creating Dropdowns
subjects = StringVar(ws)
subjects.set(subject[0])
subject_input = OptionMenu( frame , subjects , *subject )
difficulties = StringVar(ws)
difficulties.set(difficulty[0])
difficulty_input = OptionMenu( frame , difficulties , *difficulty ) 
format_input = Listbox( frame, selectmode='multiple' ) 
for format in question_format:
    format_input.insert(question_format.index(format)+1, format)

# Creating entry for # of questions
questionnumber_input = Entry(frame)

# Creating Generate Exam button
generateExam_button = Button(frame, text="Generate Exam", command=switch_to_exportExam, cursor="mouse")
generateExam_button.bind("<Return>", lambda event: switch_to_exportExam())

# Creating Log Out button
logout_button = Button(frame, text="Log Out", command=logout, cursor="mouse")
logout_button.bind("<Return>", lambda event: logout())


# Placement of text boxes and buttons
logout_button.grid(row=0, column=0, padx=10, pady=10)
subject_input.grid(row=1, column=1, padx=10, pady=10)
difficulty_input.grid(row=2, column=1, padx=10, pady=10)
questionnumber_input.grid(row=3, column=1, padx=5, pady=5)
format_input.grid(row=4, column=1, padx=10, pady=10)
generateExam_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()