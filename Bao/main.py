from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import json
from tkinter import Menu

window = Tk()
window.title("Đăng Ký Tài khoản")
window.geometry("1366x768")  # Set the size of the window
window.configure(background="light gray")

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)


users = json.load(open("users.json"))
messagebox.showinfo("users", users)
def signup():
     username = entry1_username.get()
     password = entry2_pass.get()

    # Check if username already exists
     if any(user[0] == username for user in users):  
          messagebox.showinfo("Sign up", "User already exists")
     else:
          messagebox.showinfo("Sign up", "Sign up successful")
          users.append({"username": username, "password": password})  # Update list in memory
          
label1 = Label(window, text="ĐĂNG KÝ TÀI KHOẢN", borderwidth=2, relief="solid", bg="light gray", fg="black", font="Times 20", padx=50, pady=7, justify='center', anchor='center')
label1.pack(side=TOP, pady=20)  # Use pack with side=TOP to place it at the top and pady to adjust vertical padding

label2 = Label(window, text="Họ và Tên:", bg="light gray", font="Times 25")
label2.place(x=100, y=200)

label3 = Label(window, text="Tên đăng nhập:", bg="light gray", font="Times 25")
label3.place(x=100, y=300)

label4 = Label(window, text="Mật khẩu:", bg="light gray", font="Times 25")
label4.place(x=100, y=400)

label5 = Label(window, text="Địa chỉ email:", bg="light gray", font="Times 25")
label5.place(x=100, y=500)

label6 = Label(window, text="Quốc Gia:", bg="light gray", font="Times 25")
label6.place(x = 650, y=200 )

entry_name = Entry(window, bd=4, width=35)
entry_name.place(x=310, y=210)  

entry1_username = Entry(window, bd=4, width=35)
entry1_username.place(x=310, y=310)  

entry2_pass = Entry(window, bd=4, width=35)
entry2_pass.place(x=310, y=410)  

entry3_email = Entry(window, bd=4, width=35)
entry3_email.place(x=310, y=510) 

btn = Button(window, text="Sign Up", relief="solid", font=("Times new roman", 15), width=10, height=3, fg="Blue", bg="pink", command= signup)
btn.pack()
btn.place(relx=0.5, y=600, anchor=CENTER)  # Use relx=0.5 and anchor=CENTER to center the button horizontally

combo = Combobox(window, font=("Times New Roman",15))
combo["values"]= ("Nhật Bản", "Trung Quốc", "Việt Nam", "Campuchia", "Hàn Quốc", "Tây Ban Nha")
combo.current(3)
combo.place(x = 850, y=210 )

ima = Image.open(r"D:\Teky\sat_1400\9RAQ3dMtpTNlxW7G_2023923151535.jpg")
ima = ima.resize((300,300))
photo = ImageTk.PhotoImage(ima)
labe = Label(image=photo)
labe.place(x = 850, y= 310)



window.mainloop()
