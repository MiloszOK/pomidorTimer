from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


def startTimer():
    countDown(5*60)

def countDown(czas):
    countMin = math.floor(czas/60)
    countSec = czas % 60
    if countSec < 10:
        countSec = f'0{countSec}'

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if czas > 0:
        window.after(1000, countDown, czas - 1)

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

button2 = Button(text='RESET')
button2.grid(row = 2, column = 2)

ptaszek = Label(text='✔', font=('Courier', 15, 'bold'), fg=GREEN, bg=YELLOW)
ptaszek.grid(row = 3, column = 1)



window.mainloop()

