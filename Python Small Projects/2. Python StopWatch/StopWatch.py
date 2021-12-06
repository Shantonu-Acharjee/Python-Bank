from tkinter import *
from tkinter.ttk import *

sc = 0
mn = 0
hr = 0
stp = 0

def start():
    global sc,mn,hr
    sc = sc + 1
    if (sc == 60):
        mn = mn + 1
        sc = 0

    if(mn == 60):
        hr = hr + 1
        mn = 0

    if(stp == 0):
        lbl = Label(root, text = '%i : %i : %i' %(hr, mn, sc), font = ('arial', 30, 'bold'),
        foreground = 'red', background = 'black', width = 10)
        lbl.after(300, start)
        lbl.place(x = 50, y = 60)
    

def stop():
    global stp
    stp = 1

root = Tk(); style = Style()
root.title('StopWatch')
root.geometry('210x160')
root.resizable(False, False)
root.configure(bg = 'black')

style.configure('TButton', font = ('arial', 10, 'bold'), borderwidth = '5')

button1 = Button(root, text = 'Start', command = start).place(x = 10, y = 10)
button2 = Button(root, text = 'Stop', command = stop).place(x = 100, y = 10)


root.mainloop()