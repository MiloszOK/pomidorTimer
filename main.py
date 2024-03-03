from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomidor')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=360,height=360, bg="#f7f5dd", highlightthickness=0)
obraz = PhotoImage(file='pngtree-red-fresh-tomato-with-green-leaf-png-image_6561484.png')
canvas.create_image(180,180, image=obraz)
canvas.create_text(180,200, text='00:00', fill='white', font=('Courier', 35, 'bold'))
canvas.pack()



window.mainloop()

