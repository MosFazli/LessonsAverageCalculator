# Import the required libraries
import tkinter.ttk
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.geometry("700x800")
win.configure(bg='light grey')
win.attributes("-fullscreen", True)


a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scores = []
weights = []
count = 0


def cal_sum():
    global scores
    global weights
    global a
    global b
    global count
    sum = 0
    x = 0
    for i in range(0, count):
        sum += float(a[i].get()) * float(b[i].get())
        x = x + float(b[i].get())

    label.config(text=sum / x)


# Create an Entry widget
def add():
    global a
    global b
    global scores
    global weights
    global count

    Label(win, text="Score", font=('Calibri 10')).pack(pady=(10, 0))
    a[count] = (Entry(win, width=35))
    a[count].pack()

    # scores.append(int(a.get()))
    Label(win, text="Weight", font=('Calibri 10')).pack()
    b[count] = (Entry(win, width=35))
    b[count].pack()


    # weights.append(int(b.get()))
    count = count + 1


label = Label(win, text="Total Sum : ", font=('Calibri 15'))
label.pack(pady=20)

Button(win, text="Add", command=add).pack()
Button(win, text="Calculate", command=cal_sum).pack()
Button(win, text="Exit", command=win.destroy).pack()

win.mainloop()
