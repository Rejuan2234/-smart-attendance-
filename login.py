from tkinter import *
from tkinter import messagebox
import main


def login_system():

    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":

        root.destroy()
        main.open_main()

    else:
        messagebox.showerror(
            "Login Failed",
            "Wrong Username or Password"
        )


# Window
root = Tk()

root.title("Admin Login")
root.geometry("350x250")
root.resizable(False, False)
root.configure(bg="white")


Label(
    root,
    text="SMART ATTENDANCE SYSTEM",
    font=("Arial", 16, "bold"),
    fg="blue",
    bg="white"
).pack(pady=20)


Label(
    root,
    text="Username",
    bg="white",
    font=("Arial", 12)
).pack()


user_entry = Entry(
    root,
    width=30
)

user_entry.pack(pady=5)


Label(
    root,
    text="Password",
    bg="white",
    font=("Arial", 12)
).pack()


pass_entry = Entry(
    root,
    width=30,
    show="*"
)

pass_entry.pack(pady=5)


Button(
    root,
    text="Login",
    width=20,
    height=2,
    command=login_system
).pack(pady=20)


root.mainloop()