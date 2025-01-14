from tkinter import *
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    label_file_explorer.configure(text="File Opened: " + filename)

window = Tk()
window.title('File Explorer')
window.geometry("500x500")
window.config(background="white")

label_file_explorer = Label(window, text="File Explorer using Tkinter", width=100, height=4, fg="blue")
button_explore = Button(window, text="Browse Files", command=browseFiles)
button_exit = Button(window, text="Exit", command=exit)

label_file_explorer.grid(column=1, row=1)
button_explore.grid(column=1, row=2)
button_exit.grid(column=1, row=3)

window.mainloop()
