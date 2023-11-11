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
reps = 0
timer_count = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    tick.config(text="")
    start["state"] = "normal"


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps <= 8:
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 8 == 0:
            timer.config(text="Break", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            timer.config(text="Break", fg=PINK)
            count_down(short_break_sec)
        else:
            timer.config(text="Work", fg=GREEN)
            count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    start["state"] = "disabled"
    reset["state"] = "normal"

    minutes = count // 60
    sec = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for n in range(2, reps, 2):
            marks += "✅︎"
            tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=30, bg=YELLOW)

timer = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", width=10, pady=5, highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", width=10, pady=5, highlightthickness=0, command=reset_timer, state="disabled")
reset.grid(column=3, row=3)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
tick.grid(column=1, row=4)

window.mainloop()
