from tkinter import *
import tkinter as tk
from tkinter import messagebox

def solve_equation():
    try:
        a = float(entrya.get())
        b = float(entryb.get())
        x = -b / a
        messagebox.showinfo("Kết quả", f"Nghiệm của phương trình là: x = {x}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Vui lòng nhập số hợp lệ!\n{e}")

def show_window():
    window_login = Toplevel(window)  
    window_login.title("PT bậc 1")
    window_login.geometry("500x600")

    Label(window_login, text="Nhập hệ số a:").pack()
    global entrya
    entrya = Entry(window_login)
    entrya.pack()

    Label(window_login, text="Nhập hệ số b:").pack()
    global entryb
    entryb = Entry(window_login)
    entryb.pack()

    solve_btn = Button(window_login, text="Giải phương trình", font=("Times new roman",12), fg="red", bg="light gray", command=solve_equation)
    solve_btn.pack()


window = Tk()
window.title("Máy tính")
window.geometry("500x600")
window.configure(background="light gray")

Label1 = Label(window, text="Giải Phương Trình", borderwidth=2, relief="solid", bg="light gray", fg="Black", font="Times 18", padx=30, pady=5, justify='center', anchor='center')
Label1.place(x=150, y=100)

# Nút để mở cửa sổ phương trình bậc 1
btn = Button(window, text="PT bậc 1", relief="solid", font=("Times new roman",15), width=10, height=3, fg="red", bg="light gray", command=show_window)
btn.place(x=100, y=300)

btn1 = Button(window, text="PT bậc 2", relief="solid", font=("Times new roman",15), width=10, height=3, fg="red", bg="light gray")
btn1.place(x=300, y=300)

window.mainloop()