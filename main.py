from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
rep = 0
timer = 'None'

def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text='00:00')
    tytul.config(text='Pomidorowy Timer')
    global rep
    rep = 0

def startTimer():
    global rep
    rep += 1

    workSec = 25*60
    shortBreak = 5*60
    longBreak = 20*60

    if rep % 8 == 0:
        countDown(longBreak)
        tytul.config(text='Przerwa', fg=RED)
    elif rep % 2 == 0:
        countDown(shortBreak)
        tytul.config(text='Przerwa', fg=PINK)
    else:
        countDown(workSec)
        tytul.config(text='Praca', fg=GREEN)

def countDown(czas):
    countMin = math.floor(czas/60)
    countSec = czas % 60
    if countSec < 10:
        countSec = f'0{countSec}'

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if czas > 0:
        global timer
        timer = window.after(1000, countDown, czas - 1)
    else:
        startTimer()

window = Tk()
window.title('Pomidor')
window.config(padx=100, pady=50, bg=YELLOW)

tytul = Label(text = 'Pomidorowy Timer', bg = YELLOW, fg=GREEN, font=('Courier', 35, 'bold'))
tytul.grid(row = 0, column = 1)

canvas = Canvas(width=360,height=360, bg="#f7f5dd", highlightthickness=0)
obraz = PhotoImage(file='pngtree-red-fresh-tomato-with-green-leaf-png-image_6561484.png')
canvas.create_image(180,180, image=obraz)
timerText = canvas.create_text(180,200, text='00:00', fill='white', font=('Courier', 35, 'bold'))
canvas.grid(row=1, column = 1)


button1 = Button(text='START', command=startTimer)
button1.grid(row = 2, column = 0)

button2 = Button(text='RESET', command=resetTimer)
button2.grid(row = 2, column = 2)



window.mainloop()

