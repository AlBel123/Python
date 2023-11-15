from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(numbers) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for number in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(website_name.get()) <= 0:
        messagebox.showinfo(title="Input Error", message="Website name should not be empty.")
    elif len(email_entry.get()) <= 0:
        messagebox.showinfo(title="Input Error", message="Email/User name should not be empty.")
    elif len(password_entry.get()) <= 0:
        messagebox.showinfo(title="Input Error", message="Password name should not be empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation request",
                                       message=f"The entered data are \n\n Website: {website_name.get()}\n User name: {email_entry.get()}\n "
                                               f"Password: {password_entry.get()}\n\n Do you want to save?")
        if is_ok:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{website_name.get()} | {email_entry.get()} | {password_entry.get()} \n")
                website_name.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password_Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
locker = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_name = Entry(width=35)
website_name.focus()
website_name.grid(row=1, column=1, columnspan=2, sticky="ew")

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=3, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=4, column=1, sticky="ew")

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=4, column=2, sticky="ew")

add = Button(text="Add", command=save)
add.grid(row=5, column=1, columnspan=2, sticky="ew")
window.mainloop()
