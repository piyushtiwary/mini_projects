from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
sets = 0
ticks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global sets
    global ticks
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
    canvas.itemconfig(create_canvas, text="00:00")
    sets = 0
    ticks = ""
    check_marks.config(text=ticks)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global sets
    global ticks
    sets += 1
    long_break_sec = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    if sets % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=GREEN)
    elif sets % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=RED)
        ticks += "✔"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(create_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        check_marks.config(text=ticks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
create_canvas = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(highlightthickness=0, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=3)


window.mainloop()
