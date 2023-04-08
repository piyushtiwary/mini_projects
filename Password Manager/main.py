from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers_of_numbers = 2
    numbers_of_symbols = 2
    numbers_of_letters = 4

    random_list = []
    password = ""

    for i in range(numbers_of_letters):
        random_list += random.choice(letters)

    for j in range(numbers_of_numbers):
        random_list += random.choice(numbers)

    for k in range(numbers_of_symbols):
        random_list += random.choice(symbols)

    random.shuffle(random_list)

    for char in random_list:
        password += char
    entry3.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    new_data = {
        website: {
            "email": email,
            "pass": password
        }
    }

    if len(website) == 0 or len(email) == 0:
        messagebox.showwarning("Warning", message="You left a field empty")

    else:
        try:
            with open("data.json", "r") as file_object:
                data = json.load(file_object)
        except FileNotFoundError:
            with open("data.json", "w") as file_object:
                json.dump(new_data, file_object, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file_object:
                json.dump(data, file_object, indent=4)

        entry3.delete(0, END)
        entry2.delete(0, END)
        entry1.delete(0, END)

# ---------------------------- Search ------------------------------- #


def search():
    website = entry1.get()

    try:
        with open("data.json", "r") as data_file:
            my_dic = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No Entries Found")
    else:
        if website in my_dic:
            email = my_dic[website]["email"]
            password = my_dic[website]["pass"]
            messagebox.showinfo(title=website, message=f"email: {email}\npassword: {password}")

        else:
            messagebox.showwarning(title="Warning", message="No Website found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)
entry1 = Entry(width=20)
entry1.focus()
entry1.grid(column=1, row=1)

search_button = Button(text="Search", width=20, command=search)
search_button.grid(column=2, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)
entry2 = Entry(width=45)
entry2.grid(column=1, row=2, columnspan=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)
entry3 = Entry(width=20)
entry3.grid(column=1, row=3)

generate = Button(text="Generate Password", width=20, pady=0, padx=0, command=gen_pass)
generate.grid(column=2, row=3)

button = Button(text="Add", width=36, command=add_data)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()
