import time
from tkinter import *
from tkinter import messagebox

# Create Tk window
root = Tk()

# Set geometry of the window
root.geometry("300x250")

# Title for the window
root.title("Time Counter")

# Declare variables for the time inputs
hour = StringVar()
minute = StringVar()
second = StringVar()

# Set default values
hour.set("00")
minute.set("00")
second.set("00")

# Entry widgets for user input
hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=180, y=20)

def submit():
    try:
        # Convert input to total seconds
        total_seconds = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
        return

    while total_seconds > -1:
        # Calculate the time components
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)

        # Format and update the variables
        hour.set(f"{hours:02d}")
        minute.set(f"{mins:02d}")
        second.set(f"{secs:02d}")

        # Update the window
        root.update()
        time.sleep(1)

        if total_seconds == 0:
            messagebox.showinfo("Time Countdown", "Time's up")

        # Decrement the total time
        total_seconds -= 1

# Button to start the countdown
btn = Button(root, text='Start Countdown', bd='5', command=submit)
btn.place(x=90, y=120)

# Run the Tkinter event loop
root.mainloop()
