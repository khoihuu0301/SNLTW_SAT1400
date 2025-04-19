from tkinter import *
from tkinter import messagebox
def window_options():
    window = Tk()
    window.tk
    window.title("Giải phương trình")
    window.geometry("600x800")
    window.configure(background="light gray")
    lbl_1 = Label(window, text="Select the type of equation to solve", font=("Arial", 16)).pack(pady=20)
    btn_b1 = Button(window, text = "Linear equation", font = ("Arial", 20)).pack(pady=30)
    btn_b2 = Button(window, text = "Linear equation", font = ("Arial", 20)).pack(pady=30)
    window.mainloop()

