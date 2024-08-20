from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
NO_LOOPS_YET = ""
FIRST_LOOP = "✔"
SECOND_LOOP = "✔✔"
THIRD_LOOP = "✔✔✔"
FORTH_LOOP = "✔✔✔✔"
START_TIMER = 25
LOOP_STATE = [NO_LOOPS_YET, FIRST_LOOP, SECOND_LOOP, THIRD_LOOP, FORTH_LOOP]
reset = False
timer_id = None
index = 1
print_index = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_b():
    global timer_id
    timer_text.config(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)
    v_text.config(text=" ")
    canvas.itemconfig(timer, text="00:00")
    global index
    index = 1
    window.after_cancel(timer_id)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def another_cycle():
    global print_index
    global index
    if index % 8 == 0:

        index = 0
        print_index += 1
        timer_text.config(text="BREAK", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
        count_down(25, 0)
        v_text.config(text=LOOP_STATE[print_index])

    if index % 2 == 0:
        print_index += 1
        timer_text.config(text="BREAK", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
        count_down(5, 0)
        v_text.config(text=LOOP_STATE[print_index])

    else:
        timer_text.config(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
        count_down(25, 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(*args):
    global timer_id
    global index

    minutes = args[0]
    sec = args[1]
    minutes_print = minutes
    sec_print = sec

    if sec < 10:
        sec_print = f"0{sec}"
    if minutes < 10:
        minutes_print = f"0{minutes}"

    canvas.itemconfig(timer, text=f"{minutes_print}: {sec_print}")

    if sec == 0 and minutes != 0:
        minutes -= 1
        sec = 59

    if minutes == 0 and sec == 0:
        index += 1
        window.after_cancel(timer_id)
        another_cycle()

    if sec != 0:
        timer_id = window.after(1000, count_down, minutes, sec - 1)


######################################################################################################################
# this part to init the window and background color  #


window = Tk()

window.title("pomodoro clock")
window.config(padx=100, pady=100, bg=YELLOW)

timer_text = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)

v_text = Label(text=FIRST_LOOP, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
v_text.grid(column=1, row=2)

tomato = PhotoImage(file="tomato.png")  # crate a object from photopigment class
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # create the canvas object
canvas.create_image(100, 112, image=tomato)  # notice we used the tomato object inside so the creation image

timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)  # localize on the grid

restart_b = Button(text="reset", command=reset_b)
restart_b.grid(column=2, row=2, )

start_b = Button(text="start", command=lambda: count_down(25, 0))
start_b.grid(column=0, row=2)

window.mainloop()  # keep the looping
