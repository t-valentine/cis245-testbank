from tkinter import *
import tkinter.messagebox as msg

def logout():
    ws.destroy()
    import login

# Initiate GUI

ws = Tk()
ws.title("CIS 245 Testbank Application")
ws.geometry("500x500")
ws.columnconfigure(5)


frame = Frame(ws)

# Creating Labels
Label(frame, text="Exam Generated", padx=15, pady=15).grid(row=0, column=2, sticky=W)

# Creating Log Out button
logout_button = Button(frame, text="Log Out", command=logout, cursor="mouse")
logout_button.bind("<Return>", lambda event: logout())


# Placement of text boxes and buttons
logout_button.grid(row=0, column=0, padx=10, pady=10)

frame.pack()

if __name__ == "__main__":
    ws.mainloop()