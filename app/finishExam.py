from tkinter import *
from tkinter import filedialog
import os
import requests
import tkinter.messagebox as msg

def logout():
    ws.destroy()
    import login

# Switch to exam generation page
def switch_to_generateExam():
    ws.destroy()
    import generateExam

def download_test():
    # The test results should be saved and then put into a document
    generated_test = 'example question with multiple choice answers: \n a. \n b. \n c. \n d.'
    local_test = 'test.txt'
    path = filedialog.askdirectory()

    dir_path = path
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Create file within the directory
    file_path = os.path.join(dir_path, "test.txt")
    with open(file_path, 'w') as file:
        file.write("This is an example.")

# Initiate GUI

ws = Tk()
ws.title("CIS 245 Testbank Application")
ws.geometry("500x500")

frame = Frame(ws)

# Creating Labels
Label(frame, text="Exam Generated", padx=15, pady=15).grid(row=0, column=1, sticky=W)
Label(frame, text="You can download the test using the button below, or generate a new exam by clicking the 'New Exam' button.", padx=15, pady=15, wraplength = 400).grid(row=1, column=0, columnspan=2, sticky=W)

# Creating Log Out button
logout_button = Button(frame, text="Log Out", command=logout, cursor="mouse")
logout_button.bind("<Return>", lambda event: logout())

# Creating Download button
download_button = Button(frame, text="Download Test", command=download_test, cursor="mouse")
download_button.bind("<Return>", lambda event: download_test())

# Creating Restart button
restart_button = Button(frame, text="Create New Test", command=switch_to_generateExam, cursor="mouse")
restart_button.bind("<Return>", lambda event: switch_to_generateExam())

# Placement of text boxes and buttons
download_button.grid(row=2, column=0, columnspan= 2, padx=10, pady=10)
restart_button.grid(row=3, column=0, columnspan= 2,padx=10, pady=10)
logout_button.grid(row=0, column=0, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()