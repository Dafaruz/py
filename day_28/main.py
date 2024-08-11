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
FIRST_LOOP = "✔"
SECOND_LOOPS = "✔✔"
THIRD_LOOP = "✔✔✔"
FORTH_LOOP = "✔✔✔✔"
START_TIMER = 25
LOOP_STATE = [FIRST_LOOP, SECOND_LOOPS, THIRD_LOOP, FORTH_LOOP]
index = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    another_cycle(-1)
    
# ---------------------------- TIMER MECHANISM ------------------------------- #


def another_cycle(index):
    index += 1
    v_text.config(text=LOOP_STATE[index])
    if index == 4:
        count_down(24, 59)
    else:
        count_down(5, 0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(*args):
    minutes = args[0]
    sec = args[1]
    canvas.itemconfig(timer, text=f"{minutes}: {sec}")
    if sec == 0:
        minutes -= 1
        sec = 59
    if minutes == 0:
        another_cycle(index)
    window.after(1000, count_down, min, sec-1)
# this part to init the window and background color  #


window = Tk()

window.title("pomodoro clock")
window.config(padx=100, pady=100, bg=YELLOW)

timer_text = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)

v_text = Label(text=FIRST_LOOP, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
v_text.grid(column=1, row=2)


tomato = PhotoImage(file="tomato.png")  # crate a object from photoyoimage class
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)       # create the canvas object
canvas.create_image(100, 112, image=tomato)                                # notice we used the tomato object inside so the create image method would understand the argument
timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")   # timer will be an intent with the canvas object
canvas.grid(column=1, row=1)          # localize on the grid


restart_b = Button(text="reset", command=reset)
restart_b.grid(column=2, row=2,)


start_b = Button(text="start", command=lambda: count_down(24, 59))
start_b.grid(column=0, row=2)

window.mainloop()       # keep the looping
