import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Menu

def check_login():
    username = entry_username.get()
    passwords = entry_passwords.get()
    if username =="Ctuonggdvo"and passwords =="ctuonggdvo05":
        messagebox.showinfo("Đăng nhập thành công!","chào mừng bạn đến website")
    else:
        messagebox.showerror("Đăng nhập không thành công! Vui lòng nhập lại tên hoặc mật khẩu")
window = tk.Tk()
window.title("login")



menu=Menu(window)
window.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label='file',menu=file_menu)
file_menu.add_command(label="exit",command=window.quit)



    
label_passwords=Label(window,text="passwords")
label_passwords.pack(pady=110)

entry_passwords= tk.Entry(window, width=30, show="*")
entry_passwords.pack(pady=10)

    
label_username=Label(window,text="nhập tên")
label_username.pack(pady=10)

entry_username= tk.Entry(window, width=30)
entry_username.pack(pady=10)
btn=Button(window,text="login",relief="solid"
            ,font=("Times new roman",14,"bold")
            ,width=15,height=1,fg="green"
            ,command=check_login)


btn.pack()



window.mainloop()